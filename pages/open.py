from src.components.open.page.openWidget import OpenWidget
from src.tools.log import Log


class Open(OpenWidget):
    def __init__(self, main):
        super().__init__(main)

        self.openHjButton.clicked.connect(self._loadHjWork)

    def _loadHjWork(self):
        Log.info(self, "한전 불러오기")
        self.main.work.loadHjSignal.emit()