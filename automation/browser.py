import webbrowser
from urllib.parse import quote


class Browser:

    def open_google(self):

        webbrowser.open("https://google.com")
        return "Opening Google."

    def open_youtube(self):
        webbrowser.open("https://youtube.com")
        return "Opening YouTube."

    def search_google(self, query):
        url = f"https://www.google.com/search?q={quote(query)}"
        webbrowser.open(url)

        return f"Searching Google for {query}."

    def search_youtube(self, query):
        url = f"https://www.youtube.com/results?search_query={quote(query)}"
        webbrowser.open(url)

        return f"Searching YouTube for {query}."