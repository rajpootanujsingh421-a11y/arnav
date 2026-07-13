import json
import re

from agent.tasks import Task


class TaskParser:

    def parse(self, text):

        try:

            match = re.search(r"\[.*\]", text, re.S)

            if match:
                text = match.group(0)

            data = json.loads(text)

            tasks = []

            for item in data:

                tasks.append(
                    Task(
                        item["type"],
                        **item.get("data", {})
                    )
                )

            return tasks

        except Exception as e:

            print("[TaskParser Error]", e)

            return []