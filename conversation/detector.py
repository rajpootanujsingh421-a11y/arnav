from conversation.intents import ConversationIntents


class ConversationDetector:

    def detect(self, text):

        text = text.lower().strip()

        # Greetings
        if text in [
            "hello",
            "hi",
            "hii",
            "hey",
            "namaste",
        ]:
            return ConversationIntents.GREETING

        # Good Morning
        if text in [
            "good morning",
        ]:
            return ConversationIntents.GOOD_MORNING

        # Good Afternoon
        if text in [
            "good afternoon",
        ]:
            return ConversationIntents.GOOD_AFTERNOON

        # Good Evening
        if text in [
            "good evening",
        ]:
            return ConversationIntents.GOOD_EVENING

        # Status
        if text in [
            "how are you",
            "how r u",
            "how are u",
            "how r you",
            "kaise ho",
            "kya haal hai",
            "aur bhai",
        ]:
            return ConversationIntents.STATUS

        # Thanks
        if text in [
            "thanks",
            "thank you",
            "shukriya",
            "dhanyawad",
        ]:
            return ConversationIntents.THANKS

        # Good Night
        if text in [
            "good night",
            "goodnight",
            "gn",
        ]:
            return ConversationIntents.GOOD_NIGHT

        # Goodbye
        if text in [
            "bye",
            "goodbye",
            "see you",
            "see you later",
            "bye bye",
        ]:
            return ConversationIntents.GOODBYE

        # Identity
        if text in [
            "who are you",
            "tum kaun ho",
            "tum kon ho",
            "what is your name",
            "whats your name",
            "tumhara naam kya hai",
        ]:
            return ConversationIntents.IDENTITY

        # Creator
        if text in [
            "who created you",
            "who made you",
            "kisne banaya",
            "tumhe kisne banaya",
        ]:
            return ConversationIntents.CREATOR

        return ConversationIntents.UNKNOWN