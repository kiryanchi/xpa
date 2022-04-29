from PySide6.QtWidgets import QListWidget


class WorkList(QListWidget):
    def __init__(self):
        super().__init__()

    def addList(self):
        pass

    def hideList(self):
        self.hide()

    def showList(self):
        self.show()