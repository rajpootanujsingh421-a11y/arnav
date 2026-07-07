from personality.personality import Personality
class ConversationSkill:
    
    def __init__(self):
        self.personality = Personality()
    
    def handle(self, user_input):

        text = user_input.strip().lower()

        greetings = [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ]

        if text in greetings:

            if text == "good morning":
                return f"Good morning, {self.personality.owner}! 😊 Hope you have an amazing day."

            elif text == "good evening":
                return f"Good evening, {self.personality.owner}! How was your day?"

            elif text == "good afternoon":
                return f"Good afternoon, {self.personality.owner}!"

            return f"Hello {self.personality.owner}! 👋"

        elif text in ["thanks", "thank you"]:

            return f"You're always welcome, {self.personality.owner}! 😊"

        elif text in ["how are you", "how are you?"]:

            return f"I'm doing great! Thanks for asking. How are you?"

        elif text in ["bye", "goodbye"]:

            return f"Goodbye {self.personality.owner}! Take care."

        return None