from PySide6 import QtGui
from PySide6.QtWidgets import QStackedWidget

from src.components.work.table.hjTableWidget import HjTableWidget
from src.components.work.table.gjTableWidget import GjTableWidget

from src.tools.log import Log


class WorkStacked(QStackedWidget):
    def __init__(self):
        super().__init__()

    def addWork(self, excel):
        excelType = {
            "HJ": HjTableWidget,
            "GJ": GjTableWidget
        }
        Log.info(self, f"{excelType[excel.__class__.__name__]} 테이블 추가")
        self.addWidget(excelType[excel.__class__.__name__](excel))

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
