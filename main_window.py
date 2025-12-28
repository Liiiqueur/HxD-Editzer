import os

from PyQt5.QtWidgets import (
    QMainWindow, QFileDialog, QTabWidget,
    QWidget, QHBoxLayout, QSplitter
)
from PyQt5.QtCore import Qt

from menu.file_menu import FileMenu
from toolbar.main_toolbar import MainToolBar
from viewer.viewer_bar import ViewerBar
from status.status_bar import AppStatusBar
from info.info_panel import InfoPanel   # ⚠️ 경로 맞게 수정

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HxD Editor")
        self.resize(1000, 600)

        self.init_ui()

    def init_ui(self):
        # ===== Menu =====
        self.file_menu = FileMenu(self)
        self.setMenuBar(self.file_menu)

        # ===== Tabs =====
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.on_tab_changed)

        # ===== Info Panel =====
        self.info_panel = InfoPanel()

        # ===== Splitter =====
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.tabs)
        splitter.addWidget(self.info_panel)
        splitter.setStretchFactor(0, 4)
        splitter.setStretchFactor(1, 1)

        # ===== Central Widget =====
        central = QWidget()
        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(splitter)
        self.setCentralWidget(central)

        # ===== Status Bar =====
        self.status_bar = AppStatusBar(self)
        self.setStatusBar(self.status_bar)

        # ===== Signals =====
        self.file_menu.new_action.triggered.connect(self.new_file)
        self.file_menu.open_action.triggered.connect(self.open_file)

    # ======================
    # Actions
    # ======================

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "파일 열기",
            "",
            "All Files (*)"
        )
        if not file_path:
            return

        with open(file_path, "rb") as f:
            data = f.read()

        viewer = ViewerBar(file_path, parent=self.tabs)
        viewer.load_hex(data)

        filename = os.path.basename(file_path)
        self.tabs.addTab(viewer, filename)
        self.tabs.setCurrentWidget(viewer)

    def new_file(self):
        viewer = ViewerBar(parent=self.tabs)
        self.tabs.addTab(viewer, "Untitled")
        self.tabs.setCurrentWidget(viewer)

    def close_tab(self, index):
        widget = self.tabs.widget(index)
        if widget:
            widget.deleteLater()
        self.tabs.removeTab(index)

    def on_tab_changed(self, index):
        viewer = self.tabs.widget(index)
        if viewer:
            self.info_panel.update_from_viewer(viewer)

