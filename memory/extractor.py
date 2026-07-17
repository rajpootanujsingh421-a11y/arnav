import re


class MemoryExtractor:

    def extract(self, text: str):

        text = text.strip()

        memory = []

        # NAME
        for pattern in [
            r"my name is\s+(.+)",
            r"call me\s+(.+)",
            r"mera naam\s+(.+?)\s+hai",
        ]:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                memory.append({
                    "type": "identity",
                    "key": "name",
                    "value": match.group(1).strip()
                })

                break

        
        # AGE
        for pattern in [
            r"i am (\d+) years old",
            r"i'm (\d+)",
            r"my age is (\d+)",
        ]:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                memory.append({
                    "type": "identity",
                    "key": "age",
                    "value": match.group(1)
                })

                break

        # CITY
        for pattern in [
            r"i live in (.+)",
            r"i am from (.+)",
            r"my city is (.+)",
        ]:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                memory.append({
                    "type": "identity",
                    "key": "city",
                    "value": match.group(1).strip()
                })

                break

        # PROFESSION
        for pattern in [
            r"i am a (.+)",
            r"my profession is (.+)",
        ]:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                memory.append({
                    "type": "identity",
                    "key": "profession",
                    "value": match.group(1).strip()
                })

                break
            
        # GOAL
        for pattern in [
            r"my goal is (.+)",
            r"i want to (.+)",
        ]:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                memory.append({
                    "type": "goal",
                    "key": "goal",
                    "value": match.group(1).strip()
                })

                break
            
        # DREAM
        for pattern in [
            r"my dream is (.+)",
        ]:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                memory.append({
                    "type": "goal",
                    "key": "dream",
                    "value": match.group(1).strip()
                })

                break

        # LIKES
        for pattern in [
            r"i like (.+)",
            r"i love (.+)",
            r"mujhe (.+) pasand hai",
        ]:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                memory.append({
                    "type": "preference",
                    "key": "likes",
                    "value": match.group(1).strip()
                })

                break
            print("Extracted Memory =", memory)
        return memory