from PySide6.QtWidgets import QStackedWidget

from src.components.work.table.hjTableWidget import HjTableWidget
from src.components.work.table.gjTableWidget import GjTableWidget

from src.tools.log import Log


class WorkStacked(QStackedWidget):
    def __init__(self, work):
        super().__init__()
        self.work = work

    def addWork(self, excel):
        excelType = {
            "HJ": HjTableWidget,
            "GJ": GjTableWidget
        }
        Log.info(self, f"{excelType[excel.__class__.__name__]} 테이블 추가")
        self.addWidget(excelType[excel.__class__.__name__](excel))
