class EmotionSkill:
    
    def __init__(self, memory):
        self.memory = memory

    def handle(self, user_input):

        text = user_input.lower()

        happy_words = [
            "happy",
            "great",
            "awesome",
            "excited",
            "good"
        ]

        sad_words = [
            "sad",
            "upset",
            "depressed",
            "cry",
            "bad"
        ]

        for word in happy_words:
            if word in text:
                self.memory.emotional.remember("emotion", "happy")
                return "I'm really happy to hear that! 😊"

        for word in sad_words:
            if word in text:
                self.memory.emotional.remember("emotion", "sad")
                return "I'm sorry you're feeling that way. I'm here for you. 💙"

        return None