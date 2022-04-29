from PySide6.QtWidgets import QListWidget


class WorkListWidget(QListWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main