from urllib import request

from PySide6.QtWidgets import QMessageBox

from src.components.setting.page.settingWidget import SettingWidget
from src.tools.config import Config
from src.tools.log import Log


class Setting(SettingWidget):
    def __init__(self, main):
        super().__init__(main)
        self.currentLabel.setText(main.currentVersion)
        self.latestLabel.setText(main.latestVersion)

        self.conf = Config()

        self.hj = self.conf.config['hj']
        self.gj = self.conf.config['gj']

        self.loadConfig()

        self.savePushButton.clicked.connect(self.saveSetting)

    def loadConfig(self):
        self.gjWidthLineEdit.setText(self.gj['width'])
        self.gjHeightLineEdit.setText(self.gj['height'])
        self.hjWidthLineEdit.setText(self.hj['width'])
        self.hjHeightLineEdit.setText(self.hj['height'])


    def saveSetting(self):
        if not (self.hjWidthLineEdit.text() and self.hjHeightLineEdit.text() and self.gjWidthLineEdit.text() and self.gjHeightLineEdit.text()):
            QMessageBox.warning(self, '값이 없음', '크기 값이 비어있습니다. 다시 확인해주세요.')
            return
        self.hj['width'] = self.hjWidthLineEdit.text()
        self.hj['height'] = self.hjHeightLineEdit.text()
        self.gj['width'] = self.gjWidthLineEdit.text()
        self.gj['height'] = self.gjHeightLineEdit.text()

        self.conf.save()

