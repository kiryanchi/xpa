from PySide6.QtWidgets import QWidget

from src.components.work import Ui_WorkWidget
from src.components.work.list.workList import WorkList
from src.components.work.stacked.workStacked import WorkStacked


class WorkWidget(QWidget, Ui_WorkWidget):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.main = main

        self.workList = WorkList()
        self.workStacked = WorkStacked()
        self.gridLayout.addWidget(self.workStacked)
