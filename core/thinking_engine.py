class ThinkingEngine:
    
    def __init__(self, brain):
        self.brain = brain
        
    def think(self, user_input):
# Skill
        try:
            response = self.brain.skill_manager.execute(user_input)
            
            if response:
                self.brain.memory.short.add("assistant", response)
                return response
            
        except Exception as e:
            print(f"[Skill Error] {e}")
            return "Oops! Something went while processing your request."

#Router        
        try:
            intent = self.brain.intent.detect(user_input)
            response = self.brain.router.execute(intent)

        except Exception as e:
            print(f"[Router Error] {e}")
            return "Sorry, I couldn't process that request."
        
#AI
        if response == "Sorry, I don't understand that command.":
    
            prompt = self.brain.prompt_builder.build(user_input)

            response = self.brain.provider.generate(prompt)

            response = self.brain.validator.validate(response)

        self.brain.memory.short.add("assistant", response)

        return response