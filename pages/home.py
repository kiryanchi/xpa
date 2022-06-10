from PySide6.QtWidgets import QMenu

from src.tools.log import Log

from src.components.home import HomeWidget


class Home(HomeWidget):
    def __init__(self, main):
        super().__init__(main)

        self.gjMenu = QMenu()
        self.hjMenu = QMenu()

        for menu in (self.gjMenu, self.hjMenu):
            for text in ('새로 만들기', '열기'):
                menu.addAction(text)

        self.gjMenu.triggered.connect(lambda action: self._onMenuTriggered(action, self.gjButton))
        self.hjMenu.triggered.connect(lambda action: self._onMenuTriggered(action, self.hjButton))

        self.gjButton.setMenu(self.gjMenu)
        self.hjButton.setMenu(self.hjMenu)

    def _onMenuTriggered(self, action, button):
        if action.text() == '새로 만들기':
            if button.text() == "한전":
                self.main.work.createHjSignal.emit()
            elif button.text() == '경주':
                self.main.work.createGjSignal.emit()

        elif action.text() == '열기':
            if button.text() == '한전':
                self.main.work.loadHjSignal.emit()
            elif button.text() == '경주':
                self.main.work.loadGjSignal.emit()

    def _handleHjButtonClicked(self):
        menu = QMenu()
        menu.addAction("새로 만들기")
        menu.addAction("열기")
        self.hjButton.setMenu(menu)

        return True
