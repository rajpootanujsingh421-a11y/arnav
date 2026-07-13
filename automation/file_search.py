import os

class FileSearcher:

    def find_file(self, filename):

        roots = [

            os.path.join(os.path.expanduser("~"), "Desktop"),
            os.path.join(os.path.expanduser("~"), "Documents"),
            os.path.join(os.path.expanduser("~"), "Downloads"),
            os.path.join(os.path.expanduser("~"), "Pictures"),
            os.path.join(os.path.expanduser("~"), "Videos"),
            os.path.join(os.path.expanduser("~"), "Music"),

        ]
        print("Searching:", filename)

        filename = filename.lower()

        for root in roots:
            
            print("Checking:", root)

            if not os.path.exists(root):
                continue

            for path, dirs, files in os.walk(root):
                
                for file in files:

                    if filename == file.lower():
                        print("FOUND:", os.path.join(path, file))

                        return os.path.join(path, file)
                    
        print("NOT FOUND")

        return None