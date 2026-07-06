class IntentDetector:
    
    def detect(self, text: str):

        text = text.lower().strip()

        greetings = [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good evening",
            "good afternoon",
            "namaste"
        ]

        if text in greetings:
            return "greeting"

        if "time" in text:
            return "time"

        if "date" in text:
            return "date"

        if text == "exit":
            return "exit"

        return "unknown"