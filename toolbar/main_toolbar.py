# toolbar/main_toolbar.py
from PyQt5.QtWidgets import QToolBar, QAction

class MainToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__("Main Toolbar", parent)

        self.open_action = QAction("Open", self)
        self.addAction(self.open_action)
