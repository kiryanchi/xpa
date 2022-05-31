from urllib import request
from src.components.setting.page.settingWidget import SettingWidget
from src.tools.log import Log


class Setting(SettingWidget):
    def __init__(self, main):
        super().__init__(main)

        self.loadVersion()

    def loadVersion(self):
        with open('./static/version', 'r') as f:
            currentVersion = f.readline()

        with request.urlopen('https://raw.githubusercontent.com/kiryanchi/xpa/main/static/version') as u:
            latestVersion = u.read()
            latestVersion = str(latestVersion).split("'")[1]

        self.currentLabel.setText(currentVersion)
        self.latestLabel.setText(str(latestVersion))

        print(currentVersion == latestVersion)
