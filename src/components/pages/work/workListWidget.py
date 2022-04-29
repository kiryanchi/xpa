from PySide6.QtWidgets import QListWidget

from src.components import MyQtWidget


class WorkListWidget(QListWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main