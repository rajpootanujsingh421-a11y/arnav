class ContextEngine:
    def __init__(self):
        
        self.last_intent = None
        self.last_skill = None
        self.last_topic = None
        self.last_response = None
        
        
    def update(
        self,
        intent,
        skill,
        topic,
        response
    ):
        self.last_intent = intent
        self.last_skill = skill
        self.last_topic = topic
        self.last_response = response
        
        print("\n========== CONTEXT ==========")
        print("Intent :", self.last_intent)
        print("Skill  :", self.last_skill)
        print("Topic  :", self.last_topic)
        print("Response :", self.last_response)
        print("=============================\n")
        
    def get_topic(self):
        return self.last_topic
    def get_skill(self):
        return self.last_skill
    def get_intent(self):
        return self.last_intent
    def get_response(self):
        return self.last_response
    
    def clear(self):
        
        self.last_intent = None
        self.last_skill = None
        self.last_topic = None
        self.last_response = None