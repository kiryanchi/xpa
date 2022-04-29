from PySide6.QtWidgets import QWidget

from src.components.home import Ui_HomeWidget


class HomeWidget(QWidget, Ui_HomeWidget):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.main = main
