from personality.personality import Personality
from core.text_normalizer import TextNormalizer
class ConversationSkill:
    
    def __init__(self, memory):
        self.personality = Personality()
        self.memory = memory
        self.normalizer = TextNormalizer()
        
    def get_owner(self):
        name = self.memory.get_name()
        
        if name:
            return name
        return self.personality.owner
        
    def handle(self, user_input):

        text = self.normalizer.normalize(user_input)

        greetings = [   
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ]
        
        status_queries = [

            "how are you",
            "how are you?",
            "kaise ho",
            "kaise ho?",
            "kaise ho arnav",
            "kya haal hai",
            "aur bhai",
            "aur bhai?",
            "how's it going",
            "whats up",
            "what's up",

        ]
        
        thanks_words = [

            "thanks",
            "thank you",
            "thankyou",
            "thx",
            "shukriya",
            "dhanyawad",
            "thank you so much",

        ]
        
        bye_words = [

            "bye",
            "goodbye",
            "see you",
            "see you later",
            "good night",
            "bye bye",
            "chal milte hain",
            "milte hain",
            "phir milte hain",

        ]
        
        identity_questions = [

            "who are you",
            "who are you?",
            "tum kaun ho",
            "tum kaun ho?",
            "what is your name",
            "what's your name",
            "tumhara naam kya hai",
            "apna introduction do",

        ]

        if text in greetings:

            if text == "good morning":
                return f"Good morning, {self.get_owner()}! 😊 Hope you have an amazing day."

            elif text == "good evening":
                return f"Good evening, {self.get_owner()}! How was your day?"

            elif text == "good afternoon":
                return f"Good afternoon, {self.get_owner()}!"

            response = f"Hello {self.get_owner()}! 👋"

            return response

        elif text in thanks_words:
    
            return f"You're always welcome, {self.get_owner()}! 😊"
        
        elif text in status_queries:

            return f"I'm doing great , {self.get_owner()}! 😊 How are you?"
        
        elif text in bye_words:
    
            return f"Goodbye {self.get_owner()}! Take care. 👋"
        
        elif text in identity_questions:
    
            return (
                f"I am {self.personality.name}, "
                f"your personal AI assistant. 😊 "
                f"I'm here to help you with coding, automation, "
                f"learning, files, and much more."
            )
        
        elif text == "what is my mood":
            mood = self.memory.emotional.recall("emotion")

            if mood:
                return f"Your current mood is {mood}."

            return "I don't know your mood yet."

        return None