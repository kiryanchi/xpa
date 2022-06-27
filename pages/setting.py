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

        self.hj = self.main.conf.values.hj
        self.gj = self.main.conf.values.gj

        self.loadConfig()

        self.savePushButton.clicked.connect(self.saveSetting)

    def loadConfig(self):
        self.gjWidthLineEdit.setText(str(self.gj.width))
        self.gjHeightLineEdit.setText(str(self.gj.height))
        self.hjWidthLineEdit.setText(str(self.hj.width))
        self.hjHeightLineEdit.setText(str(self.hj.height))

    def saveSetting(self):
        if not (
                self.hjWidthLineEdit.text() and self.hjHeightLineEdit.text() and self.gjWidthLineEdit.text() and self.gjHeightLineEdit.text()):
            QMessageBox.warning(self, '값이 없음', '크기 값이 비어있습니다. 다시 확인해주세요.')
            return
        self.hj.width = self.hjWidthLineEdit.text()
        self.hj.height = self.hjHeightLineEdit.text()
        self.gj.width = self.gjWidthLineEdit.text()
        self.gj.height = self.gjHeightLineEdit.text()

        self.main.conf.export('./static/config.json')
