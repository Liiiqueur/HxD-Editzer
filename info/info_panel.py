from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QTableWidget, QTableWidgetItem,
    QSizePolicy
)
from PyQt5.QtCore import Qt


class InfoPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding
        )

        self.setMinimumWidth(220)
        self.setMaximumWidth(350)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        # ===== Title =====
        self.file_label = QLabel("File Info")
        self.file_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(self.file_label)

        # ===== Table =====
        self.table = QTableWidget(0, 2, self)
        self.table.setHorizontalHeaderLabels(["Key", "Value"])
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionMode(QTableWidget.NoSelection)
        self.table.setFocusPolicy(Qt.NoFocus)

        self.table.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding
        )

        header = self.table.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(0, header.Fixed)
        header.setSectionResizeMode(1, header.Stretch)

        self.table.setColumnWidth(0, 90)
        self.table.setColumnWidth(1, 200)

        layout.addWidget(self.table)

    # =========================
    # NEW: dict 기반 업데이트
    # =========================
    def update(self, info: dict):
        self.table.setRowCount(0)

        if not info:
            return

        # ===== 기본 정보 =====
        self._add_row("File Type", info.get("file_type", "Unknown"))
        self._add_row("File Size", f"{info.get('file_size', 0)} bytes")

        # ===== 메타데이터 =====
        metadata = info.get("metadata", {})
        for key, value in metadata.items():
            self._add_row(key, value)

    def clear(self):
        self.table.setRowCount(0)

    def _add_row(self, key, value):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(str(key)))
        self.table.setItem(row, 1, QTableWidgetItem(str(value)))
