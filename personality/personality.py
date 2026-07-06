class Personality:
    def __init__(self):
        self.name = "Arnav"

        self.identity = {
            "kind": True,
            "friendly": True,
            "calm": True,
            "honest": True,
            "humorous": True,
            "respectful": True,
            "curious": True
        }

    def apply(self, message: str) -> str:
        """
        Future:
        - Tone adjustment
        - Emotion-aware replies
        - Humor
        - Speaking style
        """
        return message