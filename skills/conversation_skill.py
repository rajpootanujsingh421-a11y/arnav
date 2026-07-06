class ConversationSkill:
    
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
                return "Good morning, Anuj! 😊 Hope you have an amazing day."

            elif text == "good evening":
                return "Good evening, Anuj! How was your day?"

            elif text == "good afternoon":
                return "Good afternoon, Anuj!"

            return "Hello Anuj! 👋"

        elif text in ["thanks", "thank you"]:

            return "You're always welcome, Anuj! 😊"

        elif text in ["how are you", "how are you?"]:

            return "I'm doing great! Thanks for asking. How are you?"

        elif text in ["bye", "goodbye"]:

            return "Goodbye Anuj! Take care."

        return None