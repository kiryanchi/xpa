from PySide6.QtWidgets import QTableWidgetItem

from src.components.work.table import WorkTableWidget


class GjTableWidgetItem(QTableWidgetItem):
    def __init__(self):
        super().__init__()


class GjTableWidget(WorkTableWidget):
    def __init__(self, main):
        super().__init__(main)