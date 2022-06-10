from PySide6 import QtGui
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QMenu

from src.tools.log import Log


class WorkList(QListWidget):
    def __init__(self, work):
        super().__init__()
        self.work = work

        self.itemClicked.connect(self.handleListWidgetClicked)

    def contextMenuEvent(self, event):
        self.handleListWidgetClicked()
        menu = QMenu(self)
        delete = menu.addAction('삭제')

        action = menu.exec_(self.mapToGlobal(event.pos()))

        if action == delete:
            self.takeItem(self.currentRow())
            self.work.workStacked.removeWidget(self.work.workStacked.currentWidget())
            print(f"delete {self.currentRow()}")


    def handleListWidgetClicked(self):
        self.work.workStacked.setCurrentIndex(self.currentRow())

    def addWork(self, excel):
        item = QListWidgetItem(QIcon("./static/icon/xlsx.png"), excel.name)
        self.addItem(item)

    def hideList(self):
        self.hide()

    def showList(self):
        self.show()
