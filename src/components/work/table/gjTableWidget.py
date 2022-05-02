from PySide6.QtWidgets import QTableWidgetItem

from src.components.work.table.workTableWidget import WorkTableWidget


class GjTableWidgetItem(QTableWidgetItem):
    def __init__(self):
        super().__init__()


class GjTableWidget(WorkTableWidget):
    def __init__(self, excel):
        super().__init__(excel, 0, 3)