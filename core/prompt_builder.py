class PromptBuilder:
    
    def __init__(self, memory, personality, context):
        self.memory = memory
        self.personality = personality
        self.context = context

    def build(self, user_input):

        name = self.memory.get_name()

        if not name:
            name = "User"
            
        emotion = self.memory.emotional.recall("emotion")

        if not emotion:
            emotion = "neutral"

        history = self.context.get_recent_messages()

        conversation = ""

        for item in history:
            conversation += f"{item['role']}: {item['content']}\n"

        prompt = f"""
You are {self.personality.name}.

Never say you are Gemini, Google AI or an AI language model.

You are a personal AI assistant.

Owner: {name}

Personality:
- Friendly
- Calm
- Honest
- Helpful
- Intelligent

Current Emotion:
{emotion}

Recent Conversation:
{conversation}

User:
{user_input}
"""

        return prompt