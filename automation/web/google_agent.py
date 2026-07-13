from urllib.parse import quote


class GoogleAgent:

    def __init__(self, browser):

        self.browser = browser

    def search(self, query):

        self.browser.ensure_browser()

        url = (
            "https://www.google.com/search?q="
            + quote(query)
        )

        self.browser.page.goto(url)

        self.browser.page.wait_for_load_state()

        return f"Searching Google for {query}."