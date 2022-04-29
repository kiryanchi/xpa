from PySide6.QtWidgets import QTableWidget

from src.components import MyQtWidget


class WorkTableWidget(QTableWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
