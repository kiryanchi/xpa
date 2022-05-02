from PySide6.QtWidgets import QWidget

from src.components.open.page.Ui_openWidget import Ui_OpenWidget


class OpenWidget(QWidget, Ui_OpenWidget):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.main = main