import subprocess


class WindowsAppDatabase:

    def __init__(self):

        self.apps = {}

        self.load()

    def load(self):

        command = [
            "powershell",
            "-Command",
            "Get-StartApps"
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        lines = result.stdout.splitlines()

        for line in lines:

            line = line.strip()

            if not line:
                continue

            if line.startswith("Name"):
                continue

            if line.startswith("----"):
                continue

            parts = line.rsplit(None, 1)

            if len(parts) != 2:
                continue

            name = parts[0].strip().lower()
            appid = parts[1].strip()

            self.apps[name] = appid

    def find(self, app_name):

        app_name = app_name.lower().strip()

        # Exact Match
        if app_name in self.apps:
            return self.apps[app_name]

        # Partial Match
        for name, appid in self.apps.items():

            if app_name in name:
                return appid

        return None