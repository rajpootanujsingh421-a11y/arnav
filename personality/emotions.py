class EmotionEngine:
    
    def detect(self, text: str) -> str:

        text = text.lower()

        if any(word in text for word in ["happy", "great", "awesome"]):
            return "happy"

        if any(word in text for word in ["sad", "upset", "tired"]):
            return "sad"

        return "neutral"