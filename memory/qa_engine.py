class MemoryQAEngine:
    
    QUESTIONS = {

        "name": [
            "what is my name",
            "who am i",
            "mera naam kya hai",
        ],

        "age": [
            "how old am i",
            "meri age kya hai",
        ],

        "city": [
            "where do i live",
            "where am i from",
            "mera city kya hai",
        ],

        "goal": [
            "what is my goal",
            "what's my goal",
            "mera goal kya hai",
        ],

        "dream": [
            "what is my dream",
            "mera dream kya hai",
        ],

        "profession": [
            "what is my profession",
            "what do i do",
        ],

        "likes": [
            "what do i like",
            "mujhe kya pasand hai",
        ],

    }

    def detect(self, text):

        text = text.lower().strip()

        for key, questions in self.QUESTIONS.items():

            if text in questions:
                return key

        return None