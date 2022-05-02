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

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()


class HjTableWidgetItemImage(WorkTableWidgetItem):
    def __init__(self, img_data, hjTableWidget):
        super().__init__()
        Log.debug(self, img_data)
        self.img_data = img_data
        self.hjTableWidget = hjTableWidget
        self.image = QLabel()
        self.setImage(self.img_data)

    def setImage(self, img_data):
        if img_data is None:
            self.image.clear()
            return
        self.img_data = img_data
        data = QByteArray(self.img_data)
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        cell = self.hjTableWidget.cellWidget(0, 1)
        pixmap = pixmap.scaled(cell.width(), cell.height())
        self.image.setPixmap(pixmap)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        self.setImage(self.img_data)

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        Log.debug(self, "이미지 드롭")
        extension = ['jpg', 'png', 'jpeg', 'JPG', 'PNG', 'JPEG']
        url = event.mimeData().urls()[0]
        url = str(url.toLocalFile())
        if url.split('.')[-1] in extension:
            with open(url, 'rb') as f:
                self.img_data = f.read()
            self.setImage(self.img_data)


class HjTableWidget(WorkTableWidget):
    def __init__(self, excel):
        super().__init__(excel, 0, 4)
        self.setHorizontalHeaderLabels(['작업내역/선로번호/전산화번호', '명찰', '전경', '근접'])
        self.init()

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
