from PySide6.QtWidgets import QWidget, QMessageBox
from urllib import request
from urllib import error

from pages.home import Home
from pages.open import Open
from pages.work import Work
from pages.setting import Setting
from src.components.main import MainWidget

from src.tools.config import Config


class Main(MainWidget):
    def __init__(self):
        self.latestVersion = None
        self.currentVersion = None
        self.loadVersion()
        self.conf = Config('./static/config.json')
        super().__init__(Home(self), Work(self), Setting(self))

        if self.currentVersion != self.latestVersion:
            if self.latestVersion == 'Offline':
                QMessageBox.information(self, '인터넷 연결 안 됨', '인터넷이 연결되지 않았습니다. 업데이트를 확인할 수 없습니다.')
                return
            QMessageBox.information(self, '업데이트 있음', '업데이트가 있습니다. 최신 버전을 다운받아주세요.')

    def loadVersion(self):
        with open('./static/version', 'r') as f:
            self.currentVersion = f.readline()

        try:
            with request.urlopen('https://raw.githubusercontent.com/kiryanchi/xpa/main/static/version') as u:
                self.latestVersion = u.read()
                self.latestVersion = str(self.latestVersion).split("'")[1]

        except error.URLError:
            self.latestVersion = 'Offline'
