from PySide6 import QtGui
from PySide6.QtCore import QByteArray
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QVBoxLayout, QLineEdit, QLabel

from src.components.work.table.workTableWidget import WorkTableWidget, WorkTableWidgetItem
from src.tools.log import Log


class HjTableWidgetItemText(WorkTableWidgetItem):
    def __init__(self, 내역):
        super().__init__()
        self.작업내역 = QLineEdit(내역['작업내역'])
        self.선로번호 = QLineEdit(내역['선로번호'])
        self.전산화번호 = QLineEdit(내역['전산화번호'])

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.작업내역)
        self.layout().addWidget(self.선로번호)
        self.layout().addWidget(self.전산화번호)


class HjTableWidgetItemImage(WorkTableWidgetItem):
    def __init__(self, img_data, hjTableWidget):
        super().__init__()
        Log.debug(self, img_data)
        self.imgData = img_data
        self.hjTableWidget = hjTableWidget
        self.image = QLabel()
        self.setImage(self.imgData)

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self.image)

    def setImage(self, imgData):
        self.imgData = imgData
        if imgData is None:
            self.image.clear()
            return
        data = QByteArray(self.imgData)
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        cell = self.hjTableWidget.cellWidget(0, 1)
        pixmap = pixmap.scaled(cell.width(), cell.height())
        self.image.setPixmap(pixmap)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        self.setImage(self.imgData)

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        if event.mimeData().hasUrls():
            extension = ['jpg', 'png', 'jpeg', 'JPG', 'PNG', 'JPEG']
            url = event.mimeData().urls()[0].toLocalFile()
            Log.debug(self, url)
            if url.split('.')[-1] in extension:
                with open(url, 'rb') as f:
                    self.imgData = f.read()
                self.setImage(self.imgData)


class HjTableWidget(WorkTableWidget):
    def __init__(self, excel):
        super().__init__(excel, 0, 4)
        self.setHorizontalHeaderLabels(['작업내역/선로번호/전산화번호', '명찰', '전경', '근접'])
        self.init()

    def addRow(self, index=None):
        if index is None:
            index = self.rowCount()

        self.insertRow(index)
        self.excel.addLine(index)

    def init(self):
        for i in range(self.excel.row):
            self.addRow()

        for i in range(self.excel.row):
            self.setRowWidget(i, *self.excel.getLine(i))

    def setRowWidget(self, row, 내역, 명찰, 전경, 근접):
        Log.debug(self, f"{내역}")

        tableItemWidgets = [
            HjTableWidgetItemText(내역),
            HjTableWidgetItemImage(명찰, self),
            HjTableWidgetItemImage(전경, self),
            HjTableWidgetItemImage(근접, self)
        ]
        for i in range(len(tableItemWidgets)):
            Log.debug(self, f"{row},{i} 에 {tableItemWidgets[i]}")
            self.setCellWidget(row, i, tableItemWidgets[i])
