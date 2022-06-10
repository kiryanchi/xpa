from PySide6.QtWidgets import QWidget

from pages.home import Home
from pages.open import Open
from pages.work import Work
from src.components.main import MainWidget


class Main(MainWidget):
    def __init__(self):
        super().__init__(Home(self), Work(self))
