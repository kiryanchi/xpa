from PySide6.QtWidgets import QWidget

from src.components.work.table.Ui_workInnerWidget import Ui_WorkInnerWidget
from src.components.work.table.gjTableWidget import GjTableWidget
from src.components.work.table.hjTableWidget import HjTableWidget
from src.tools.log import Log


class WorkInnerWidget(QWidget, Ui_WorkInnerWidget):
    def __init__(self, excel):
        super().__init__()
        self.setupUi(self)
        self.excel = excel
        self.tableWidget = None

        self.addTableWidget()
        self.addButton.clicked.connect(lambda: self.tableWidget.addRow())
        self.removeButton.clicked.connect(lambda: self.tableWidget.deleteRow(self.tableWidget.currentRow()))
        self.saveButton.clicked.connect(lambda: self.excel.save())

    def addTableWidget(self):
        excelType = {
            "HJ": HjTableWidget,
            "GJ": GjTableWidget,
        }
        Log.info(self, f"{excelType[self.excel.__class__.__name__]} 테이블 추가")
        self.tableWidget = excelType[self.excel.__class__.__name__](self.excel)
        self.layout().addWidget(self.tableWidget)