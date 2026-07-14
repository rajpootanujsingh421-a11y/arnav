class ThinkingEngine:
    
    def __init__(self, brain):
        self.brain = brain

    def think(self, user_input):

# Skills
        try:

            response = self.brain.skill_manager.execute(user_input)

            if response:

                self.brain.memory.short.add(
                    "assistant",
                    response
                )

                return response

        except Exception as e:

            print(f"[Skill Error] {e}")

# Planner (AI Agent)
        
        try:

            tasks = self.brain.local_planner.create_plan(user_input)

            if tasks:

                print("⚡ Local Planner")

                response = self.brain.executor.execute(tasks)

                self.brain.memory.short.add(
                    "assistant",
                    response
                )

                return response

        except Exception as e:

            print(f"[Local Planner Error] {e}")

# Gemini Planner (Fallback)
        try:

            tasks = self.brain.planner.create_plan(user_input)

            if tasks:

                print("🧠 Gemini Planner")

                response = self.brain.executor.execute(tasks)

                self.brain.memory.short.add(
                    "assistant",
                    response
                )

                return response

        except Exception as e:

            print(f"[Planner Error] {e}")
            
# Router
        try:

            intent = self.brain.intent.detect(user_input)

            response = self.brain.router.execute(intent)

            if response:

                self.brain.memory.short.add(
                    "assistant",
                    response
                )

                return response

        except Exception as e:

            print(f"[Router Error] {e}")

# AI Chat
        try:

            prompt = self.brain.prompt_builder.build(user_input)

            raw_response = self.brain.provider.generate(prompt)

            parsed = self.brain.response_parser.parse(raw_response)

            response = self.brain.validator.validate(
                parsed["response"]
            )

            self.brain.memory.short.add(
                "assistant",
                response
            )

            return response

        except Exception as e:

            print(f"[AI Error] {e}")

            return (
                "Sorry, I'm having trouble connecting right now. "
                "Please try again in a moment."
            )