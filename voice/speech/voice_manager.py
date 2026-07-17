import time

from voice.speech.listener import Listener
from voice.speech.wake_word import WakeWord
from voice.speaker import Speaker


class VoiceManager:

    def __init__(self, assistant):

        self.assistant = assistant

        self.listener = Listener()
        self.wake = WakeWord()
        self.speaker = Speaker()

        self.timeout = 20

    def start(self):

        print("🎤 Voice Manager Started")

        while True:

            # Wait For Wake Word
            print("\n🎤 Waiting for Wake Word...")

            while True:

                text = self.listener.listen()

                if not text:
                    continue

                print("You :", text)

                if self.wake.detect(text):
                    break

            print("🤖 Wake Word Detected!")

            self.speaker.speak("Yes Anuj?")

            last_time = time.time()
            
            # Conversation Mode
            while True:

                print("🎤 Listening for command...")

                command = self.listener.listen()

                # Timeout
                if not command:

                    if time.time() - last_time > self.timeout:

                        print("😴 Going back to sleep...")

                        self.speaker.speak("Going back to sleep.")

                        break

                    continue

                last_time = time.time()

                print("Command :", command)

                response = self.assistant.process_command(command)

                print("🤖 Arnav :", response)

                self.speaker.speak(response)

                # Exit conversation
                if command.lower() in [
                    "bye",
                    "goodbye",
                    "sleep",
                    "go to sleep",
                ]:

                    self.speaker.speak("Goodbye Anuj.")

                    break