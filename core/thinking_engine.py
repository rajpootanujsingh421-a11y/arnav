class ThinkingEngine:
    
    def __init__(self, brain):
        self.brain = brain

    def think(self, user_input):
        
        # Skills
        try:

            response = self.brain.skill_manager.execute(user_input)

            if response:

                self.brain.memory.short.add("assistant", response)

                return response

        except Exception as e:

            print(f"[Skill Error] {e}")

        # Router
        try:

            intent = self.brain.intent.detect(user_input)

            response = self.brain.router.execute(intent)

        except Exception as e:

            print(f"[Router Error] {e}")

            response = None
            
        # Router Response
        if response:

            self.brain.memory.short.add("assistant", response)

            return response

        # AI Thinking
        prompt = self.brain.prompt_builder.build(user_input)

        raw_response = self.brain.provider.generate(prompt)

        parsed = self.brain.response_parser.parse(raw_response)

        response = self.brain.validator.validate(
            parsed["response"]
        )

        self.brain.memory.short.add("assistant", response)

        return response