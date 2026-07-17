class SkillRouter:
    def __init__(self):
        self.routes = {}
        
    def register(self, intent, skill):
        self.routes[intent] = skill
        
    def get(self, intent):  
        return self.routes.get(intent)