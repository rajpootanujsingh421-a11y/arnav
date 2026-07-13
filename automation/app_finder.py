import os
import shutil

ALIASES = {
    "vs code": "visual studio code",
    "code": "visual studio code",   
    "chrome": "google chrome",
    "whatsapp": "whatsapp web",
    "vlc": "vlc media player",
    "intellij": "intellij idea",
}

class AppFinder:

    def find(self, app_name):

        app_name = app_name.lower().strip()
        
        if app_name in ALIASES:
            app_name = ALIASES[app_name]

# PATH search
        path = shutil.which(app_name)

        if path:
            return path

        folders = [

            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",

            os.path.expandvars(
                r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"
            )

        ]

# Exact match
        for folder in folders:

            if not os.path.exists(folder):
                continue

            for root, _, files in os.walk(folder):

                for file in files:

                    if not file.lower().endswith(".lnk"):
                        continue

                    name = file.lower().replace(".lnk", "")

                    if name == app_name:

                        return os.path.join(root, file)

# Partial match
        for folder in folders:

            if not os.path.exists(folder):
                continue

            for root, _, files in os.walk(folder):

                for file in files:

                    if not file.lower().endswith(".lnk"):
                        continue

                    words = app_name.split()
                    if all(word in name for word in words):
                        return os.path.join(root, file)

                    if app_name in name or name in app_name:

                        return os.path.join(root, file)

        return None