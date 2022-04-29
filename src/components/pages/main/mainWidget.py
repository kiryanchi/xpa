from PySide6.QtWidgets import QWidget

from src.components.pages.main import Ui_MainWidget


class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self, homeWidget, newWidget, recentWidget, openWidget, workStackedWidget, workListWidget):
        super().__init__()
        self.setupUi(self)
        self._initWidget(homeWidget, newWidget, recentWidget, openWidget, workStackedWidget, workListWidget)
        self._addStackedWidget()
        self._connectButton()

    def _addStackedWidget(self):
        self.mainStackedWidget.addWidget(self.homeWidget)
        self.mainStackedWidget.addWidget(self.newWidget)
        self.mainStackedWidget.addWidget(self.recentWidget)
        self.mainStackedWidget.addWidget(self.openWidget)
        self.mainStackedWidget.addWidget(self.workStackedWidget)

    def _connectButton(self):
        def _switchWidget(button):
            buttonIndex = {
                "Home": 0,
                "New": 1,
                "Recent": 2,
                "Open": 3,
                "Work": 4,
            }

            self.mainStackedWidget.setCurrentIndex(buttonIndex[button.text()])

            if button.text() == "Work":
                self.workListWidget.show()

            else:
                self.workListWidget.hide()

        self.homeButton.clicked.connect(lambda: _switchWidget(self.homeButton))
        self.newButton.clicked.connect(lambda: _switchWidget(self.newButton))
        self.recentButton.clicked.connect(lambda: _switchWidget(self.recentButton))
        self.openButton.clicked.connect(lambda: _switchWidget(self.openButton))
        self.workButton.clicked.connect(lambda: _switchWidget(self.workButton))

    def _initWidget(self, homeWidget, newWidget, recentWidget, openWidget, workWidget, workListWidget):
        self.homeWidget = homeWidget
        self.newWidget = newWidget
        self.recentWidget = recentWidget
        self.openWidget = openWidget
        self.workStackedWidget = workWidget
        self.workListWidget = workListWidget
