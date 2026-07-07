class ContextEngine:
    
    def __init__(self, memory):
        self.memory = memory

    def get_recent_messages(self, limit=5):

        history = self.memory.short.get()

        return history[-limit:] 
    
    def get_last_message(self):
    
        history = self.memory.short.get()

        if not history:
            return None

        return history[-1]