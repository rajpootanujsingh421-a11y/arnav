from voice.speech.listener import Listener

listener = Listener()

while True:

    text = listener.listen()

    if text:

        print(text)