from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget, QAbstractItemView, QWidget, QHeaderView

from src.tools.log import Log


class WorkTableWidgetItem(QWidget):
    def __init__(self):
        super().__init__()

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        Log.debug(self, 'dragEnter')
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e: QtGui.QDragMoveEvent) -> None:
        Log.debug(self, 'dragMove')
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        Log.debug(self, 'dropEvent')
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()



class WorkTableWidget(QTableWidget):
    def __init__(self, excel, row, col):
        super().__init__(row, col)
        self.excel = excel

        self.setAcceptDrops(True)
        self.setSelectionMode(QAbstractItemView.SingleSelection)

        self.setAlternatingRowColors(True)
        self.setFocusPolicy(Qt.StrongFocus)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.verticalHeader().setDefaultSectionSize(self.height()//5)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

    def addRow(self, index=None):
        if index is None:
            index = self.rowCount()

        self.insertRow(index)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        self.verticalHeader().setDefaultSectionSize(event.size().height()//5)

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

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()
