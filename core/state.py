class AssistantState:
    def __init__(self):
        self.is_online = True
        self.is_listening = False
        self.is_speaking = False
        
    def show(self):
        print("Assistant State")
        print(f"Online    : {self.is_online}")
        print(f"Listening : {self.is_listening}")
        print(f"Speaking  : {self.is_speaking}")    