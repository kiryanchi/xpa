from PySide6.QtWidgets import QWidget

from src.components.pages.home import Ui_HomeWidget


class HomeWidget(QWidget, Ui_HomeWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main

        self.setupUi(self)
