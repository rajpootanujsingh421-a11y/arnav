from personality.personality import Personality
class ConversationSkill:
    
    def __init__(self, memory):
        self.personality = Personality()
        self.memory = memory
        
    def get_owner(self):
        name = self.memory.get_name()
        
        if name:
            return name
        return self.personality.owner
        
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
                return f"Good morning, {self.get_owner()}! 😊 Hope you have an amazing day."

            elif text == "good evening":
                return f"Good evening, {self.get_owner()}! How was your day?"

            elif text == "good afternoon":
                return f"Good afternoon, {self.get_owner()}!"

            return f"Hello {self.get_owner()}! 👋"

        elif text in ["thanks", "thank you"]:

            return f"You're always welcome, {self.get_owner()}! 😊"

        elif text in ["how are you", "how are you?"]:

            return f"I'm doing great! Thanks for asking. How are you?"

        elif text in ["bye", "goodbye"]:

            return f"Goodbye {self.get_owner()}! Take care."
        
        elif text == "what is my mood":
            mood = self.memory.emotional.recall("emotion")

            if mood:
                return f"Your current mood is {mood}."

            return "I don't know your mood yet."

        return None