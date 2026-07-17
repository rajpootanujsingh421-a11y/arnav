class ContextResolver:
    
    def __init__(self, context):

        self.context = context

    def resolve(self, text):

        lower = text.lower()

        last_topic = self.context.last_topic or ""

        # Pronouns / Reference words
        references = [
            "it",
            "this",
            "that",
            "there",
            "again",
            "same"
        ]

        if any(word in lower for word in references):

            if last_topic:

                return f"{last_topic} -> {text}"

        return text