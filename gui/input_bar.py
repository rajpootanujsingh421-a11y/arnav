from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
)

from gui.theme import *


class InputBar(QWidget):

    def __init__(self):

        super().__init__()

        self.build_ui()

    def build_ui(self):

        layout = QHBoxLayout()

        self.input = QLineEdit()

        self.input.setPlaceholderText("Ask Arnav anything...")

        self.input.setStyleSheet(
            f"""
            QLineEdit {{
                background:{CARD};
                color:{TEXT};
                border:2px solid {ACCENT};
                border-radius:12px;
                padding:10px;
                font-size:16px;
            }}
            """
        )

        self.send_btn = QPushButton("Send")

        self.send_btn.setStyleSheet(
            f"""
            QPushButton {{
                background:{ACCENT};
                color:black;
                font-weight:bold;
                border-radius:10px;
                padding:10px;
            }}

            QPushButton:hover {{
                background:#55E8FF;
            }}
            """
        )

        layout.addWidget(self.input)

        layout.addWidget(self.send_btn)

        self.setLayout(layout)