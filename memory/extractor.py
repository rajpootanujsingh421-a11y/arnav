import re


class MemoryExtractor:

    def extract(self, text: str):

        text = text.strip()

        memory = []

        patterns = [

            r"my name is (.+)",
            r"i am (.+)",
            r"mera naam (.+) hai",
            r"main (.+) hoon",
        ]

        for pattern in patterns:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                memory.append({
                    "type": "identity",
                    "key": "name",
                    "value": match.group(1).strip()
                })

        patterns = [

            r"i like (.+)",
            r"i love (.+)",
            r"mujhe (.+) pasand hai",
        ]

        for pattern in patterns:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                memory.append({
                    "type": "preference",
                    "key": "likes",
                    "value": match.group(1).strip()
                })

        return memory