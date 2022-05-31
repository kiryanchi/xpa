from PySide6.QtWidgets import QWidget

from src.components.setting.page.Ui_settingWidget import Ui_SettingWidget


class SettingWidget(QWidget, Ui_SettingWidget):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.main = main
