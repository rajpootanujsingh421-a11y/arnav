class WakeWord:
    
    def __init__(self):

        self.words = [
            "arnav",
            "hey arnav",
            "hello arnav",
        ]

    def detect(self, text):

        if not text:
            return False

        text = text.lower().strip()

        for word in self.words:

            if word in text:
                return True

        return False