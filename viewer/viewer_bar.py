from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtGui import QFont, QTextCursor, QTextCharFormat, QColor
from formats.registry import detect_format


class ViewerBar(QPlainTextEdit):
    BYTES_PER_LINE = 16

    def __init__(self, file_path=None, parent=None):
        super().__init__(parent)

        self.file_path = file_path
        self.data = b""
        self.hex_line_positions = []

        self.setFont(QFont("Consolas", 10))
        self.setReadOnly(True)
        self.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.fmt_addr = QTextCharFormat()
        self.fmt_addr.setForeground(QColor("#C586C0"))

        self.fmt_hex = QTextCharFormat()
        self.fmt_hex.setForeground(QColor("#000000"))

        self.fmt_ascii = QTextCharFormat()
        self.fmt_ascii.setForeground(QColor("#6A9955"))

    # =========================
    # Load & Render
    # =========================

    def new_file(self):
        self.clear()
        self.hex_line_positions.clear()

    def load_hex(self, data: bytes):
        self.clear()
        self.hex_line_positions.clear()
        self.data = data

        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.Start)
        self.verticalScrollBar().setValue(0)

        # ===== Header =====
        header = (
            "Offset(h)  "
            + " ".join(f"{i:02X}" for i in range(16))
            + "  Decoded text\n"
        )
        cursor.insertText(header, self.fmt_addr)

        # ===== Body =====
        for offset in range(0, len(data), self.BYTES_PER_LINE):
            chunk = data[offset:offset + self.BYTES_PER_LINE]

            cursor.insertText(f"{offset:08X}   ", self.fmt_addr)

            hex_start = cursor.position()
            self.hex_line_positions.append(hex_start)

            hex_part = " ".join(f"{b:02X}" for b in chunk)
            cursor.insertText(hex_part.ljust(16 * 3 - 1) + "  ", self.fmt_hex)

            ascii_part = "".join(
                chr(b) if 32 <= b <= 126 else "."
                for b in chunk
            )
            cursor.insertText(ascii_part, self.fmt_ascii)
            cursor.insertText("\n")

        self.highlight_signatures()

    # =========================
    # Highlight (Registry 기반)
    # =========================

    def highlight_signatures(self):
        analyzer = detect_format(self.data)
        if not analyzer:
            return

        for sig in analyzer.signatures:
            sig_bytes = bytes.fromhex(sig)
            start = 0

            while True:
                idx = self.data.find(sig_bytes, start)
                if idx == -1:
                    break

                for i in range(len(sig_bytes)):
                    self.highlight_hex_byte(idx + i, analyzer.color)
                    self.highlight_ascii_byte(idx + i, analyzer.color)

                start = idx + 1

    def highlight_hex_byte(self, offset, color):
        line = offset // self.BYTES_PER_LINE
        col = offset % self.BYTES_PER_LINE

        if line >= len(self.hex_line_positions):
            return

        pos = self.hex_line_positions[line] + col * 3

        cursor = self.textCursor()
        fmt = QTextCharFormat()
        fmt.setBackground(QColor(color))

        cursor.setPosition(pos)
        cursor.setPosition(pos + 2, QTextCursor.KeepAnchor)
        cursor.mergeCharFormat(fmt)

    def highlight_ascii_byte(self, offset, color):
        line = offset // self.BYTES_PER_LINE
        col = offset % self.BYTES_PER_LINE

        if line >= len(self.hex_line_positions):
            return

        ascii_start = (
            self.hex_line_positions[line]
            + (self.BYTES_PER_LINE * 3 - 1)
            + 2
        )

        pos = ascii_start + col

        cursor = self.textCursor()
        fmt = QTextCharFormat()
        fmt.setBackground(QColor(color))

        cursor.setPosition(pos)
        cursor.setPosition(pos + 1, QTextCursor.KeepAnchor)
        cursor.mergeCharFormat(fmt)

    # =========================
    # External Analysis Info
    # =========================

    def get_analysis_info(self):
        info = {
            "file_type": None,
            "file_size": len(self.data),
            "signatures": [],
            "metadata": {}
        }

        analyzer = detect_format(self.data)
        if analyzer:
            info["file_type"] = analyzer.name
            info["signatures"] = analyzer.signatures
            info["metadata"] = analyzer.extract_metadata(self.data)

        return info
