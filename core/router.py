from commands import hello, time, date, exit


class CommandRouter:

    def execute(self, command: str):

        command = command.lower().strip()

        routes = {
            "greeting": hello.execute,
            "time": time.execute,
            "date": date.execute,
            "exit": exit.execute,
        }

        action = routes.get(command)

        if action:
            return action()

        return None