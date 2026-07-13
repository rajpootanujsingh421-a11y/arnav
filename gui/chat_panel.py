from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit
)

from gui.theme import *


class ChatPanel(QWidget):

    def __init__(self):

        super().__init__()

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout()

        self.chat = QTextEdit()

        self.chat.setReadOnly(True)

        self.chat.setStyleSheet(
            f"""
            QTextEdit{{
                background:{CARD};
                color:{TEXT};
                border:2px solid {ACCENT};
                border-radius:15px;
                padding:15px;
                font-size:16px;
            }}
            """
        )

        self.chat.append("🤖 Arnav : Hello Anuj!")

        layout.addWidget(self.chat)

        self.setLayout(layout)