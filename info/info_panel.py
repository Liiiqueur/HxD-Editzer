from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QTableWidget, QTableWidgetItem,
    QSizePolicy
)
from PyQt5.QtCore import Qt


class InfoPanel(QWidget):
    def __init__(self):
        super().__init__()

        # 🔹 InfoPanel 자체는 "적당히만" 커지게
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

        # 🔥 핵심: 폭을 절대 강요하지 않게
        self.table.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding
        )

        header = self.table.horizontalHeader()
        header.setStretchLastSection(True)      # Value 컬럼만 늘어남
        header.setSectionResizeMode(0, header.Fixed)
        header.setSectionResizeMode(1, header.Stretch)

        self.table.setColumnWidth(0, 90)   # Key 고정
        self.table.setColumnWidth(1, 200)  # Value 기본 폭

        layout.addWidget(self.table)

    def update_from_viewer(self, viewer):
        """
        ViewerBar로부터 파일 메타데이터를 받아 InfoPanel에 표시
        """

        # 기존 내용 초기화
        self.table.setRowCount(0)

        # ===== 기본 정보 =====
        info = []

        # 파일 크기
        if hasattr(viewer, "data"):
            info.append(("File Size", f"{len(viewer.data)} bytes"))

        # 파일 타입 (viewer에서 계산해둔 경우)
        if hasattr(viewer, "file_type"):
            info.append(("File Type", viewer.file_type))

        # ===== 테이블에 추가 =====
        for key, value in info:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(key)))
            self.table.setItem(row, 1, QTableWidgetItem(str(value)))

