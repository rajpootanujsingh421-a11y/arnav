class PromptBuilder:
    
    def __init__(self, memory, personality, context):
        self.memory = memory
        self.personality = personality
        self.context = context

    def build(self, user_input):

        name = self.memory.get("name")

        if not name:
            name = "User"
            
        emotion = self.memory.emotional.recall("emotion")

        if not emotion:
            emotion = "neutral"

        history = self.context.get_recent_messages()
        long_memory = self.memory.long.all()

        conversation = ""

        for item in history:
            conversation += f"{item['role']}: {item['content']}\n"
            
        system_prompt = self.personality.system_prompt()

        prompt = f"""
        {system_prompt}
        
        user Profile:
        {long_memory}

        Current Emotion:
        {emotion}

        Recent Conversation:
        {conversation}

        User:
        {user_input}
        
        Respond naturally
        """

        return prompt