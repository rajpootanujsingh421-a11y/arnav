from brain.response_selector import ResponseSelector
from conversation.intents import ConversationIntents
from personality.personality import Personality


class OfflineBrain:

    def __init__(self, memory):

        self.memory = memory
        self.personality = Personality()
        self.selector = ResponseSelector()

    def reply(self, intent):

        name = self.memory.get_name()

        if not name:
            name = "Friend"

        if intent == ConversationIntents.GREETING:

            return self.selector.get(
                "greeting",
                name=name
            )

        elif intent == ConversationIntents.STATUS:

            return self.selector.get(
                "status",
                name=name
            )

        elif intent == ConversationIntents.THANKS:

            return self.selector.get(
                "thanks",
                name=name
            )

        elif intent == ConversationIntents.GOOD_NIGHT:

            return self.selector.get(
                "good_night",
                name=name
            )

        elif intent == ConversationIntents.GOODBYE:

            return self.selector.get(
                "goodbye",
                name=name
            )

        elif intent == ConversationIntents.IDENTITY:

            return self.selector.get(
                "identity",
                name=name
            )

        elif intent == ConversationIntents.CREATOR:

            return self.selector.get(
                "creator",
                name=self.personality.owner
            )

        return None