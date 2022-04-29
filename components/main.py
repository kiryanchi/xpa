from PySide6.QtWidgets import QWidget

from components.home import Home
from components.work import WorkList, WorkStacked
from src.components.pages.main import MainWidget


class Main(MainWidget):
    def __init__(self):
        super().__init__(Home(self), QWidget(), QWidget(), QWidget(), WorkStacked(self), WorkList(self))
