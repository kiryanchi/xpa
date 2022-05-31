from PySide6 import QtGui
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

from src.components.main import Ui_MainWidget
from src.tools.log import Log


class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self, homeWidget, newWidget, recentWidget, openWidget, workWidget, settingWidget):
        super().__init__()
        self.setupUi(self)
        self._buttonIcon()
        self._initWidget(homeWidget, newWidget, recentWidget, openWidget, workWidget, settingWidget)
        self._addStackedWidget()
        self._connectButton()

    def _addStackedWidget(self):
        self.mainStackedWidget.addWidget(self.home)
        self.mainStackedWidget.addWidget(self.new)
        self.mainStackedWidget.addWidget(self.recent)
        self.mainStackedWidget.addWidget(self.open)
        self.mainStackedWidget.addWidget(self.work)
        self.mainStackedWidget.addWidget(self.setting)

    def _buttonIcon(self):
        self.homeButton.setIcon(QIcon("./static/icon/home.png"))
        self.newButton.setIcon(QIcon("./static/icon/new.png"))
        self.recentButton.setIcon(QIcon("./static/icon/recent.png"))
        self.openButton.setIcon(QIcon("./static/icon/open.png"))
        self.workButton.setIcon(QIcon("./static/icon/work.png"))

    def _connectButton(self):
        def _switchWidget(button):
            buttonIndex = {
                "Home": 0,
                "New": 1,
                "Recent": 2,
                "Open": 3,
                "Work": 4,
                "Setting": 5,
            }

            Log.info(self, f"{button.text()} 전환")
            self.mainStackedWidget.setCurrentIndex(buttonIndex[button.text()])

            if button.text() == "Work":
                self.work.workList.showList()

            else:
                self.work.workList.hideList()

        self.homeButton.clicked.connect(lambda: _switchWidget(self.homeButton))
        self.newButton.clicked.connect(lambda: _switchWidget(self.newButton))
        self.recentButton.clicked.connect(lambda: _switchWidget(self.recentButton))
        self.openButton.clicked.connect(lambda: _switchWidget(self.openButton))
        self.workButton.clicked.connect(lambda: _switchWidget(self.workButton))
        self.settingButton.clicked.connect(lambda: _switchWidget(self.settingButton))

    def _initWidget(self, homeWidget, newWidget, recentWidget, openWidget, workWidget, settingWidget):
        self.home = homeWidget
        self.new = newWidget
        self.recent = recentWidget
        self.open = openWidget
        self.work = workWidget
        self.setting = settingWidget