class AutomationParser:
    
    APPS = {
        "vs code": "visual studio code",
        "vscode": "visual studio code",
        "code": "visual studio code",

        "chrome": "google chrome",
        "calculator": "calculator",
        "calc": "calculator",
        "paint": "paint",
        "notepad": "notepad",

        "whatsapp": "whatsapp",
        "camera": "camera",
        "cmd": "command prompt",
        "powershell": "windows powershell",

        "instagram": "instagram",
        "linkedin": "linkedin",
    }
    
    FOLDERS = {

    "downloads": "downloads",
    "download": "downloads",

    "desktop": "desktop",

    "documents": "documents",
    "document": "documents",

    "pictures": "pictures",
    "picture": "pictures",

    "videos": "videos",
    "video": "videos",

    "music": "music",
    "songs": "music",
}

    OPEN_WORDS = [
        "open",
        "launch",
        "start",
        "run",
        "khol",
        "kholo",
        "khol do",
        "chalu",
        "chalu karo",
        "open karo",
        "open kar do",
    ]

    def parse(self, text):

        text = text.lower().strip()

        # Browser
        if "google" in text and "search" not in text:
            return ("browser", "google")

        if "youtube" in text and "search" not in text:
            return ("browser", "youtube")
        
        # Folder
        folder = None

        for key, value in self.FOLDERS.items():

            if key in text:

                folder = value

                break

        if folder:

            for word in self.OPEN_WORDS:

                if word in text:

                    return ("folder", folder)
                
        #File
        if any(word in text for word in self.OPEN_WORDS):
            words = text.split()
            for word in words:
                if "." in word:
                    return ("file", word)

        # Agar koi app ka naam hi nahi mila
        app = None

        for key, value in self.APPS.items():
            if key in text:
                app = value
                break

        if app is None:
            return None

        # Agar kisi bhi tarah ka open word mila
        for word in self.OPEN_WORDS:
            if word in text:
                return ("dynamic_app", app)

        return None