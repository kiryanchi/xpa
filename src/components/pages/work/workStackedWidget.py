from PySide6.QtWidgets import QStackedWidget


class WorkStackedWidget(QStackedWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main