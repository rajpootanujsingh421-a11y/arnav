class ThinkingEngine:
    
    def __init__(self, brain):
        self.brain = brain

    def think(self, user_input):
        
        user_input = self.brain.context_resolver.resolve(
            user_input
        )

        # Intent Detection
        intent = self.brain.detector.detect(user_input)

        # Skill Router
        skill = self.brain.skill_router.get(intent)

        if skill:

            response = skill.handle(user_input)

            if response:

                self.brain.memory.short.add(
                    "assistant",
                    response
                )

                self.brain.context.update(
                    intent,
                    skill.__class__.__name__,
                    user_input,
                    response
                )

                return response

        # Remaining Skill
        try:

            response = self.brain.skill_manager.execute(user_input)

            if response:

                self.brain.memory.short.add(
                    "assistant",
                    response
                )

                self.brain.context.update(
                    intent,
                    "SkillManager",
                    user_input,
                    response
                )

                return response

        except Exception as e:

            print(f"[Skill Error] {e}")

        # Local Planner
        try:

            tasks = self.brain.local_planner.create_plan(user_input)

            if tasks:

                response = self.brain.executor.execute(tasks)

                self.brain.memory.short.add(
                    "assistant",
                    response
                )

                self.brain.context.update(
                    intent,
                    "LocalPlanner",
                    user_input,
                    response
                )

                return response

        except Exception as e:

            print(f"[Local Planner Error] {e}")

        # Gemini Planner
        try:

            tasks = self.brain.planner.create_plan(user_input)

            if tasks:

                response = self.brain.executor.execute(tasks)

                self.brain.memory.short.add(
                    "assistant",
                    response
                )

                self.brain.context.update(
                    intent,
                    "Planner",
                    user_input,
                    response
                )

                return response

        except Exception as e:

            print(f"[Planner Error] {e}")

        # Command Router
        try:

            command = self.brain.intent.detect(user_input)

            response = self.brain.router.execute(command)

            if response:

                self.brain.memory.short.add(
                    "assistant",
                    response
                )

                self.brain.context.update(
                    intent,
                    "CommandRouter",
                    user_input,
                    response
                )

                return response

        except Exception as e:

            print(f"[Router Error] {e}")

        # Offline Brain
        response = self.brain.offline.reply(intent)

        if response:

            self.brain.memory.short.add(
                "assistant",
                response
            )

            self.brain.context.update(
                intent,
                "OfflineBrain",
                user_input,
                response
            )

            return response

        # AI Chat
        try:

            prompt = self.brain.prompt_builder.build(user_input)

            raw = self.brain.provider.generate(prompt)

            parsed = self.brain.response_parser.parse(raw)

            response = self.brain.validator.validate(
                parsed["response"]
            )

            self.brain.memory.short.add(
                "assistant",
                response
            )

            self.brain.context.update(
                intent,
                "AI",
                user_input,
                response
            )

            return response

        except Exception:

            return (
                "Sorry, I'm having trouble connecting right now."
            )