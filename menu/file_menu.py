# menu/file_menu.py
from PyQt5.QtWidgets import QMenuBar, QAction

class FileMenu(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        file_menu = self.addMenu("File")
        self.new_action = QAction("New", self)
        self.new_action.setShortcut("Ctrl+N") 
        self.new_action.setStatusTip("새 파일 만들기")
        self.open_action = QAction("Open", self)
        self.open_action.setShortcut("Ctrl+O")
        self.new_action.setStatusTip("파일 열기")
        self.exit_action = QAction("Exit", self)

        file_menu.addAction(self.new_action)
        file_menu.addSeparator()
        file_menu.addAction(self.open_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)