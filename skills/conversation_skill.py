from personality.personality import Personality
from core.text_normalizer import TextNormalizer
from conversation.detector import ConversationDetector
from conversation.intents import ConversationIntents
from brain.response_selector import ResponseSelector


class ConversationSkill:

    def __init__(self, memory):

        self.personality = Personality()
        self.memory = memory
        self.normalizer = TextNormalizer()
        self.detector = ConversationDetector()
        self.selector = ResponseSelector()

    def get_owner(self):

        name = self.memory.get_name()

        if name:
            return name

        return self.personality.owner

    def handle(self, user_input):

        text = self.normalizer.normalize(user_input)
        intent = self.detector.detect(text)
        print("Detected Intent =", intent)

        print("🔥 Conversation Skill Running")

        if intent == ConversationIntents.GREETING:

            return self.selector.get(
                "greeting",
                name=self.get_owner()
            )

        elif intent == ConversationIntents.GOOD_MORNING:

            return self.selector.get(
                "good_morning",
                name=self.get_owner()
            )

        elif intent == ConversationIntents.GOOD_AFTERNOON:

            return self.selector.get(
                "good_afternoon",
                name=self.get_owner()
            )

        elif intent == ConversationIntents.GOOD_EVENING:

            return self.selector.get(
                "good_evening",
                name=self.get_owner()
            )

        elif intent == ConversationIntents.GOOD_NIGHT:

            return self.selector.get(
                "good_night",
                name=self.get_owner()
            )

        elif intent == ConversationIntents.STATUS:

            return self.selector.get(
                "status",
                name=self.get_owner()
            )

        elif intent == ConversationIntents.THANKS:

            return self.selector.get(
                "thanks",
                name=self.get_owner()
            )

        elif intent == ConversationIntents.GOODBYE:

            return self.selector.get(
                "goodbye",
                name=self.get_owner()
            )

        elif intent == ConversationIntents.IDENTITY:

            return self.selector.get(
                "identity",
                name=self.get_owner()
            )

        elif intent == ConversationIntents.CREATOR:

            return self.selector.get(
                "creator",
                name=self.personality.owner
            )

        return None