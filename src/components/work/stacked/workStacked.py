from PySide6.QtWidgets import QStackedWidget

from src.components.work.table.hjTableWidget import HjTableWidget
from src.components.work.table.gjTableWidget import GjTableWidget
from src.components.work.table.workInnerWidget import WorkInnerWidget

from src.tools.log import Log


class WorkStacked(QStackedWidget):
    def __init__(self, work):
        super().__init__()
        self.work = work

    def addWork(self, excel):
        self.addWidget(WorkInnerWidget(excel))
        Log.info(self, "WorkInnerWidget 테이블 추가")
