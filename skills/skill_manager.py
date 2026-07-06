class SkillManager:
    
    def __init__(self):
        self.skills = []

    def register(self, skill):
        self.skills.append(skill)

    def execute(self, user_input):

        for skill in self.skills:

            response = skill.handle(user_input)

            if response is not None:
                return response

        return None