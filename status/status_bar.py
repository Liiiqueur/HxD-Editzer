# status/status_bar.py
from PyQt5.QtWidgets import QStatusBar

class AppStatusBar(QStatusBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.showMessage("준비")

    def show_new_file(self):
        self.showMessage("새 파일이 생성되었습니다", 3000)
