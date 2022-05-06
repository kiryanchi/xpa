from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget, QAbstractItemView, QWidget, QHeaderView

from src.tools.log import Log


class WorkTableWidgetItem(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e: QtGui.QDragMoveEvent) -> None:
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()


class WorkTableWidget(QTableWidget):
    def __init__(self, excel, row, col):
        super().__init__(row, col)
        self.excel = excel

        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)

        self.setAlternatingRowColors(True)
        self.setFocusPolicy(Qt.StrongFocus)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.verticalHeader().setDefaultSectionSize(self.height()//5)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

    def resizeEvent(self, e: QtGui.QResizeEvent) -> None:
        self.verticalHeader().setDefaultSectionSize(e.size().height() // 5)
        self.horizontalHeader().setDefaultSectionSize(e.size().width() // 4)

    def dropEvent(self, e:QtGui.QDropEvent) -> None:
        currentRow = self.currentRow()
        destItem = self.itemAt(e.pos())

        print(currentRow, destItem.row())