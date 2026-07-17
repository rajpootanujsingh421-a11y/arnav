class SkillManager:
    
    def __init__(self):
        self.skills = []

    def register(self, skill):
        self.skills.append(skill)

    def execute(self, user_input):

        for skill in self.skills:

# ConversationSkill ko skip karo
            if skill.__class__.__name__ == "ConversationSkill":
                continue

            print(f"Running Skill -> {skill.__class__.__name__}")

            response = skill.handle(user_input)

            if response is not None:
                return response

        return None