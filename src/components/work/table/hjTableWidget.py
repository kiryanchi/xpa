from io import BytesIO

from PySide6 import QtGui
from PySide6.QtCore import QByteArray, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QVBoxLayout, QLineEdit, QLabel, QTableWidgetItem

from src.components.work.table.workTableWidget import WorkTableWidget, WorkTableWidgetItem
from src.tools.log import Log


class HjTableWidgetItemText(WorkTableWidgetItem):
    def __init__(self, 내역=None):
        super().__init__()
        if 내역 is None:
            self.작업내역 = QLineEdit('')
            self.선로번호 = QLineEdit('')
            self.전산화번호 = QLineEdit('')
        else:
            self.작업내역 = QLineEdit(내역['작업내역'])
            self.선로번호 = QLineEdit(내역['선로번호'])
            self.전산화번호 = QLineEdit(내역['전산화번호'])

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.작업내역)
        self.layout().addWidget(self.선로번호)
        self.layout().addWidget(self.전산화번호)

    def get내역(self):
        return {'작업내역': self.작업내역.text(),
                '선로번호': self.선로번호.text(),
                '전산화번호': self.전산화번호.text()}


class HjTableWidgetItemImage(WorkTableWidgetItem):
    def __init__(self, img_data, hjTableWidget):
        super().__init__()
        self.imgData = None
        self.pixmap = None
        self.resizeCount = 0
        self.hjTableWidget = hjTableWidget
        self.image = QLabel()
        self.setImage(img_data)

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(5, 5, 5, 5)
        self.layout().addWidget(self.image)

    def getImg(self):
        # if self.imgData:
        #     return BytesIO(self.imgData)
        return self.imgData

    def setImage(self, imgData):
        self.imgData = imgData
        if imgData.__class__.__name__ == 'Image':
            print('_data()')
            self.imgData = imgData._data()
        if imgData is None:
            print('None')
            self.imgData = imgData
            self.pixmap = None
            self.image.clear()
            return
        if self.pixmap is None:
            print('pixmap none')
            self.pixmap = QPixmap()
        data = QByteArray(self.imgData)
        self.pixmap.loadFromData(data)
        self.pixmap = self.pixmap.scaled(self.hjTableWidget.width() // 4, self.hjTableWidget.height() // 5)
        self.image.setPixmap(self.pixmap)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        if self.pixmap is not None:
            self.resizeCount += 1
            if self.resizeCount > 20:
                self.setImage(self.imgData)
                self.resizeCount = 0
                return
            self.pixmap = self.pixmap.scaled(self.hjTableWidget.width() // 4, self.hjTableWidget.height() // 5)
            self.image.setPixmap(self.pixmap)

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        if event.mimeData().hasUrls():
            extension = ['jpg', 'png', 'jpeg', 'JPG', 'PNG', 'JPEG']
            url = event.mimeData().urls()[0].toLocalFile()
            Log.debug(self, url)
            if url.split('.')[-1] in extension:
                with open(url, 'rb') as f:
                    self.imgData = f.read()
                self.setImage(self.imgData)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key_Escape:
            print("key pressed")
            print(self.hjTableWidget.currentItem())


class HjTableWidget(WorkTableWidget):
    def __init__(self, excel):
        super().__init__(excel, 0, 4)
        self.setHorizontalHeaderLabels(['작업내역/선로번호/전산화번호', '명찰', '전경', '근접'])
        self.init()
        print(self.columnCount(), self.rowCount())

    def _rowToIndex(self, row):
        return row - 2

    def addRow(self, index=None):
        if index is None:
            index = self.rowCount()

        self.insertRow(index)
        self.excel.addLine()
        self.setRowWidget(index, None, None, None, None)

    def deleteRow(self, index=None):
        if index is None:
            index = self.rowCount()

        self.excel.removeLine()
        self.removeRow(index)

    def init(self):
        self.setRowCount(self._rowToIndex(self.excel.sheet.max_row))

        for i in range(self._rowToIndex(self.excel.sheet.max_row)):
            self.setRowWidget(i, *self.excel.getLine(i))

    def save(self):
        for index in range(self._rowToIndex(self.excel.sheet.max_row)):
            self.excel.saveLine(index,
                                self.cellWidget(index, 0).get내역(),
                                self.cellWidget(index, 1).getImg(),
                                self.cellWidget(index, 2).getImg(),
                                self.cellWidget(index, 3).getImg())
        self.excel.loadImage()
        self.excel.save()

    def setRowWidget(self, row, 내역, 명찰, 전경, 근접):
        Log.debug(self, f"{내역}, {명찰}, {전경}, {근접}")

        tableItemWidgets = [
            HjTableWidgetItemText(내역),
            HjTableWidgetItemImage(명찰, self),
            HjTableWidgetItemImage(전경, self),
            HjTableWidgetItemImage(근접, self)
        ]
        for i in range(len(tableItemWidgets)):
            self.setCellWidget(row, i, tableItemWidgets[i])
            self.setItem(row, i, QTableWidgetItem())

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        current = {'row': self.currentRow(), 'column': self.currentColumn()}
        dest = {'row': self.itemAt(e.pos()).row(), 'column': self.itemAt(e.pos()).column()}
        print(current, dest)
        currentWidget = self.cellWidget(current['row'], current['column'])
        destWidget = self.cellWidget(dest['row'], dest['column'])

        if currentWidget.__class__.__name__ == 'HjTableWidgetItemText':
            if destWidget.__class__.__name__ == 'HjTableWidgetItemText':
                # line swap
                print('text')
                pass

        elif currentWidget.__class__.__name__ == 'HjTableWidgetItemImage':
            if destWidget.__class__.__name__ == 'HjTableWidgetItemImage':
                print(self.excel.images)
                currentImgData = currentWidget.imgData
                destImgData = destWidget.imgData
                currentWidget.setImage(destImgData)
                destWidget.setImage(currentImgData)
