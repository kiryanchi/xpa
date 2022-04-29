from PySide6.QtWidgets import QStackedWidget

from src.components import MyQtWidget


class WorkStackedWidget(QStackedWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main