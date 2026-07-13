from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
)

from PySide6.QtCore import Qt

from gui.theme import *
from gui.voice_ring import VoiceRing
from gui.chat_panel import ChatPanel
from gui.input_bar import InputBar


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Arnav AI")

        self.resize(1200, 700)

        self.setStyleSheet(
            f"""
            QWidget{{
                background:{BACKGROUND};
                color:{TEXT};
                font-size:18px;
            }}
            """
        )

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("ARNAV")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet(
            f"""
            font-size:40px;
            font-weight:bold;
            color:{ACCENT};
            """
        )
        ring = VoiceRing()

        status = QLabel("STATUS : ONLINE")
        
        chat = ChatPanel()
        
        input_bar = InputBar()

        status.setAlignment(Qt.AlignCenter)

        status.setStyleSheet(
            f"""
            font-size:18px;
            color:{SUCCESS};
            """
        )

        layout.addStretch()

        layout.addWidget(title)

        layout.addWidget(ring)

        layout.addSpacing(20)

        layout.addWidget(status)

        layout.addSpacing(25)

        layout.addWidget(chat)

        layout.addSpacing(15)

        layout.addWidget(input_bar)

        layout.addStretch()

        self.setLayout(layout)


if __name__ == "__main__":

    app = QApplication([])

    window = MainWindow()

    window.show()

    app.exec()