class MemoryInspectorSkill:
    
    def __init__(self, memory):
        self.memory = memory

    def handle(self, user_input):

        text = user_input.strip().lower()

        if text != "show memory":
            return None

        result = "\n========= MEMORY =========\n"

        result += "\nShort Memory\n"
        result += "------------------\n"

        for item in self.memory.short.get():
            result += f"{item['role']} : {item['content']}\n"

        result += "\nLong Memory\n"
        result += "------------------\n"

        name = self.memory.get_name()

        if name:
            result += f"Name : {name}\n"
        else:
            result += "Name : Not Saved\n"

        result += "\nEmotional Memory\n"
        result += "------------------\n"

        emotion = self.memory.emotional.recall("emotion")

        if emotion:
            result += f"Emotion : {emotion}\n"
        else:
            result += "Emotion : Unknown\n"

        result += "\n=========================="

        return result