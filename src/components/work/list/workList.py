from PySide6 import QtGui
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QListWidget, QListWidgetItem

from src.tools.log import Log


class WorkList(QListWidget):
    def __init__(self, work):
        super().__init__()
        self.work = work

        self.itemClicked.connect(self.foo)

    def foo(self):
        self.work.workStacked.setCurrentIndex(self.currentRow())

    def addWork(self, excel):
        item = QListWidgetItem(QIcon("./static/icon/xlsx.png"), excel.name)
        self.addItem(item)

    def hideList(self):
        self.hide()

    def showList(self):
        self.show()
