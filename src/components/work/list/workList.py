from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QListWidget, QListWidgetItem


class WorkList(QListWidget):
    def __init__(self):
        super().__init__()

    def addWork(self, excel):
        item = QListWidgetItem(QIcon("./static/icon/xlsx.png"), excel.name)
        self.addItem(item)

    def hideList(self):
        self.hide()

    def showList(self):
        self.show()