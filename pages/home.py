from src.tools.log import Log

from src.components.home import HomeWidget


class Home(HomeWidget):
    def __init__(self, main):
        super().__init__(main)

        self.hjButton.clicked.connect(self._addHjWork)

    def _addHjWork(self):
        Log.info(self, "한전 새 작업 시작")
        self.main.work.createHjSignal.emit()