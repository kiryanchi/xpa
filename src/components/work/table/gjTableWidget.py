from PySide6.QtCore import QByteArray
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QTableWidgetItem, QVBoxLayout, QLabel, QLineEdit

from src.components.work.table.workTableWidget import WorkTableWidget, WorkTableWidgetItem


class GjTableWidgetItem(WorkTableWidgetItem):
    def __init__(self, data, gjTableWidget):
        super().__init__()
        self.imageData = None
        self.pixmap = None
        self.resizeCount = 0
        self.gjTableWidget = gjTableWidget
        self.image = QLabel()
        self.lineEdit = QLineEdit()
        self.setImage(data['image'])
        self.setText(data['text'])

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self.lineEdit)
        self.layout().addWidget(self.image)

    def getData(self):
        return {
            'imageData': self.imageData,
            'text': self.lineEdit.text()
        }

    def setText(self, text):
        self.lineEdit.setText(text)

    def setImage(self, imageData):
        self.imageData = imageData
        if imageData.__class__.__name__ == 'Image':
            self.imageData = imageData._data()
        if imageData is None:
            self.imageData = imageData
            self.pixmap = None
            self.image.clear()
            return
        if self.pixmap is None:
            self.pixmap = QPixmap()
        data = QByteArray(self.imageData)
        self.pixmap.loadFromData(data)
        self.pixmap = self.pixmap.scaled(self.gjTableWidget.width() // 3, self.gjTableWidget.height() // 5)
        self.image.setPixmap(self.pixmap)

    def resizeEvent(self, event):
        if self.pixmap is not None:
            self.resizeCount += 1
            if self.resizeCount > 20:
                self.setImage(self.imageData)
                self.resizeCount = 0
                return
            self.pixmap = self.pixmap.scaled(self.gjTableWidget.width() // 3, self.gjTableWidget.height() // 5)
            self.image.setPixmap(self.pixmap)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            extension = ['jpg', 'png', 'jpeg', 'JPG', 'PNG', 'JPEG']
            url = event.mimeData().urls()[0].toLocalFile()
            if url.split('.')[-1] in extension:
                with open(url, 'rb') as f:
                    self.imageData = f.read()
                self.setImage(self.imageData)

class GjTableWidget(WorkTableWidget):
    def __init__(self, excel):
        super().__init__(excel, 0, 3)
        self.setHorizontalHeaderLabels(['공사전 사진/구간명', '전주 번호', '공사후 사진/공정명'])
        self.init()

    def _rowToIndex(self, row):
        return (row - 3) // 22

    def init(self):
        self.setRowCount(self._rowToIndex(self.excel.sheet.max_row))

        for i in range(self._rowToIndex(self.excel.sheet.max_row)):
            self.setRowWidget(i, self.excel.getLine(i))

    def setRowWidget(self, row, line):
        col = 0
        for key, value in line.items():
            self.setItem(row, col, QTableWidgetItem())
            self.setCellWidget(row, col, GjTableWidgetItem(value, self))
            col += 1

    def addRow(self):
        pass

    def deleteRow(self, row):
        pass

    def save(self):
        for index in range(self.rowCount()):
            self.excel.saveLine(index,
                                self.cellWidget(index, 0).getData(),
                                self.cellWidget(index, 1).getData(),
                                self.cellWidget(index, 2).getData()
                                )

        self.excel.save()


    def dropEvent(self, event):
        current = {'row': self.currentRow(), 'column': self.currentColumn()}
        dest = {'row': self.itemAt(event.pos()).row(), 'column': self.itemAt(event.pos()).column()}

        currentWidget = self.cellWidget(current['row'], current['column'])
        destWidget = self.cellWidget(dest['row'], dest['column'])

        currentImageData = currentWidget.imageData
        currentText = currentWidget.lineEdit.text()
        destImageData = destWidget.imageData
        destText = destWidget.lineEdit.text()

        currentWidget.setImage(destImageData)
        currentWidget.setText(destText)

        destWidget.setImage(currentImageData)
        destWidget.setText(currentText)

