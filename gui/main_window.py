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
from core.assistant import ArnavAssistant


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()
        self.assistant = ArnavAssistant()

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
        
        self.chat = ChatPanel()
        
        self.input_bar = InputBar()

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

        layout.addWidget(self.chat)

        layout.addSpacing(15)

        layout.addWidget(self.input_bar)

        layout.addStretch()

        self.setLayout(layout)
        
        self.input_bar.send_callback = self.send_message
        
    def send_message(self):
        
        text = self.input_bar.get_text().strip()

        if not text:
            return

        self.chat.add_message("You", text)

        response = self.assistant.process_command(text)

        self.chat.add_message("Arnav", response)

        self.input_bar.clear()

if __name__ == "__main__":

    app = QApplication([])

    window = MainWindow()

    window.show()

    app.exec()
    
    