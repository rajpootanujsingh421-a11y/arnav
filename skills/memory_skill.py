from memory.qa_engine import MemoryQAEngine


class MemorySkill:

    def __init__(self, memory):
        self.memory = memory
        self.qa = MemoryQAEngine()

    def handle(self, user_input):

        text = user_input.strip()
        lower = text.lower()

        # Save Name
        if (
            lower.startswith("my name is ")
            or lower.startswith("remember my name is ")
            or lower.startswith("call me ")
        ):

            if lower.startswith("remember my name is "):
                name = text[20:].strip()

            elif lower.startswith("call me "):
                name = text[8:].strip()

            else:
                name = text[11:].strip()

            self.memory.save_name(name)

            return f"Nice to meet you, {name}! I'll remember your name."

        # Hindi Save Name
        if lower.startswith("mera naam "):

            if "kya hai" in lower:
                return None

            name = text[10:].strip()

            if name.lower().endswith("hai"):
                name = name[:-3].strip()

            self.memory.save_name(name)

            return (
                f"Theek hai! Main yaad rakhunga "
                f"ki tumhara naam {name} hai."
            )

        # Forget Name
        if lower in [
            "forget my name",
            "mera naam bhool jao"
        ]:

            self.memory.forget_name()

            return "Okay, I've forgotten your name."

        # Memory QA Engine
        key = self.qa.detect(lower)

        if key:

            if key == "name":
                value = self.memory.get_name()
            else:
                value = self.memory.get(key)

            if value:

                responses = {

                    "name":
                        f"Your name is {value}.",

                    "age":
                        f"You are {value} years old.",

                    "city":
                        f"You live in {value}.",

                    "goal":
                        f"Your goal is {value}.",

                    "dream":
                        f"Your dream is {value}.",

                    "profession":
                        f"You are a {value}.",

                    "likes":
                        f"You like {value}.",

                }

                return responses.get(key, str(value))

            return f"I don't know your {key} yet."

        return None