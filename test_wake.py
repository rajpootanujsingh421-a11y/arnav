from voice.speech.listener import Listener
from voice.speech.wake_word import WakeWord

listener = Listener()
wake = WakeWord()

while True:

    print("🎤 Waiting for Wake Word...")

    text = listener.listen()

    if not text:
        continue

    print("You :", text)

    if wake.detect(text):
        print("🤖 Wake Word Detected!")
        break