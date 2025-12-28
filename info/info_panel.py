from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTreeWidget, QTreeWidgetItem
)

class InfoPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.file_type_label = QLabel("File Type: -")
        self.file_size_label = QLabel("File Size: -")

        self.meta_tree = QTreeWidget()
        self.meta_tree.setHeaderLabels(["Key", "Value"])

        layout.addWidget(self.file_type_label)
        layout.addWidget(self.file_size_label)
        layout.addWidget(self.meta_tree)

    def update_from_viewer(self, viewer):
        info = viewer.get_analysis_info()

        self.file_type_label.setText(
            f"File Type: {info['file_type'] or 'Unknown'}"
        )
        self.file_size_label.setText(
            f"File Size: {info['file_size']} bytes"
        )

        self.meta_tree.clear()
        for k, v in info["metadata"].items():
            QTreeWidgetItem(self.meta_tree, [k, str(v)])
