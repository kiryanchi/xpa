from PySide6.QtWidgets import QWidget
from urllib import request
from urllib import error

from pages.home import Home
from pages.open import Open
from pages.work import Work
from pages.setting import Setting
from src.components.main import MainWidget


class Main(MainWidget):
    def __init__(self):
        self.latestVersion = None
        self.currentVersion = None
        self.loadVersion()
        super().__init__(Home(self), Work(self), Setting(self))

    def loadVersion(self):
        with open('./static/version', 'r') as f:
            self.currentVersion = f.readline()

        try:
            with request.urlopen('https://raw.githubusercontent.com/kiryanchi/xpa/main/static/version') as u:
                self.latestVersion = u.read()
                self.latestVersion = str(self.latestVersion).split("'")[1]

        except error.URLError:
            self.latestVersion = 'Offline'

        if self.currentVersion != self.latestVersion:
            print('not version')
