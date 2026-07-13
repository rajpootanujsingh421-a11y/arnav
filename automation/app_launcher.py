import os
import subprocess


class AppLauncher:

    def launch(self, target):

        try:

            if target.lower().endswith(".lnk"):

                os.startfile(target)

            else:

                subprocess.Popen(target)

            return f"Opening {os.path.basename(target)}."

        except Exception as e:

            print(e)

            return "Sorry, I couldn't open that application."

    def launch_store_app(self, app_id):

        try:

            subprocess.Popen(
                [
                    "explorer.exe",
                    f"shell:AppsFolder\\{app_id}"
                ]
            )

            return "Opening application."

        except Exception as e:

            print(e)

            return "Sorry, I couldn't open that application."