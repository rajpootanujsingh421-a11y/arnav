class EmotionSkill:
    
    def __init__(self, memory):
        self.memory = memory

    def handle(self, user_input):

        text = user_input.lower().strip()

        happy_words = {
            "happy",
            "great",
            "awesome",
            "excited",
            "fantastic",
            "amazing"
        }

        sad_words = {
            "sad",
            "upset",
            "depressed",
            "cry",
            "bad"
        }

        words = set(text.split())

        if words & happy_words:

            self.memory.emotional.remember(
                "emotion",
                "happy"
            )

            return "I'm really happy to hear that! 😊"

        if words & sad_words:

            self.memory.emotional.remember(
                "emotion",
                "sad"
            )

            return (
                "I'm sorry you're feeling that way. "
                "I'm here for you. 💙"
            )

        return None