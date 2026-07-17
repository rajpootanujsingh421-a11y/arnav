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
from core.state import AssistantState   
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QThread
from gui.worker import AssistantWorker

class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.assistant = ArnavAssistant()
        self.current_state = AssistantState.IDLE

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

        # Title
        title = QLabel("🤖 ARNAV AI")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(
            f"""
            font-size:42px;
            font-weight:bold;
            color:{ACCENT};
            letter-spacing:2px;
            """
        )

        # Subtitle
        subtitle = QLabel("Personal Desktop Assistant")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet(
            f"""
            font-size:16px;
            color:{TEXT};
            """
        )

        # Voice Ring
        self.ring = VoiceRing()

        # Status
        self.status = QLabel("🟢 Idle")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setStyleSheet(
            f"""
            font-size:18px;
            font-weight:bold;
            color:{SUCCESS};
            """
        )

        # Chat
        self.chat = ChatPanel()

        # Input
        self.input_bar = InputBar()

        layout.addStretch()

        layout.addWidget(title)
        layout.addWidget(subtitle)

        layout.addSpacing(10)

        layout.addWidget(self.ring)

        layout.addSpacing(20)

        layout.addWidget(self.status)

        layout.addSpacing(25)

        layout.addWidget(self.chat)

        layout.addSpacing(15)

        layout.addWidget(self.input_bar)

        layout.addStretch()

        self.setLayout(layout)

        self.input_bar.send_callback = self.send_message

    # -------------------------

    def set_state(self, state):
        
        print("STATE =", state)

        self.current_state = state

        icons = {
            AssistantState.IDLE: "🟢",
            AssistantState.LISTENING: "🎤",
            AssistantState.THINKING: "🧠",
            AssistantState.SPEAKING: "🗣",
            AssistantState.EXECUTING: "⚙",
            AssistantState.OFFLINE: "🔴",
        }

        icon = icons.get(state, "🟢")

        self.status.setText(f"{icon} {state}")

    # -------------------------

    def send_message(self):
    
        text = self.input_bar.get_text().strip()

        if not text:
            return

        self.chat.add_message("You", text)

        self.input_bar.clear()

        self.set_state(AssistantState.THINKING)

    # Background Thread
        self.thread = QThread()

        self.worker = AssistantWorker(
            self.assistant,
            text
        )

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(
            self.worker.run
        )

        self.worker.finished.connect(
            self.on_response
        )

        self.worker.finished.connect(
            self.thread.quit
        )

        self.worker.finished.connect(
            self.worker.deleteLater
        )

        self.thread.finished.connect(
            self.thread.deleteLater
        )

        self.thread.start()
        
    def on_response(self, response):
    
        self.chat.add_message(
            "Arnav",
            response
        )

        self.set_state(
            AssistantState.IDLE
        )

if __name__ == "__main__":

    app = QApplication([])

    window = MainWindow()

    window.show()

    app.exec()