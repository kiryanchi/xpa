from urllib import request
from src.components.setting.page.settingWidget import SettingWidget
from src.tools.log import Log


class Setting(SettingWidget):
    def __init__(self, main):
        super().__init__(main)
        self.currentLabel.setText(main.currentVersion)
        self.latestLabel.setText(main.latestVersion)
