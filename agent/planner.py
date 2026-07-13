from agent.task_parser import TaskParser


class Planner:

    def __init__(self, brain):

        self.brain = brain
        self.parser = TaskParser()

    def create_plan(self, user_input):

        prompt = f"""
You are an AI Task Planner.

Convert the user request into ONLY valid JSON.

Rules:
- Return ONLY JSON.
- Do NOT explain anything.
- Do NOT use markdown.
- Do NOT write ```json.
- If no task matches, return [].

Supported Tasks:

1. youtube_search

{{
    "type":"youtube_search",
    "data": {{
        "query":"song name"
    }}
}}

2. play_first

{{
    "type":"play_first"
}}

3.google_search

{{
    "type": "google_search"
}}

4. open_app

{{
    "type":"open_app",
    "data": {{
        "target":"application name"
    }}
}}

Examples:

User:
Play Believer on YouTube

Output:

[
    {{
        "type":"youtube_search",
        "data": {{
            "query":"Believer"
        }}
    }},
    {{
        "type":"play_first"
    }}
]

User:
Search Python decorators on Google

Output:

[
    {{
        "type": "google_search",
        "data":{{
            "query":"Python decorators"
        }}
    }}
]

User:
Open VS Code

Output:

[
    {{
        "type":"open_app",
        "data": {{
            "target":"visual studio code"
        }}
    }}
]

User:
Open Chrome

Output:

[
    {{
        "type":"open_app",
        "data": {{
            "target":"google chrome"
        }}
    }}
]

User:
{user_input}

Output:
"""

        print("\n========== Planner Running ==========")

        response = self.brain.provider.generate(prompt)

        print("\n========== RAW GEMINI RESPONSE ==========")
        print(response)
        print("=========================================\n")

        tasks = self.parser.parse(response)

        print("========== Parsed Tasks ==========")

        for task in tasks:
            print(task.type, task.data)

        print("==================================")

        return tasks