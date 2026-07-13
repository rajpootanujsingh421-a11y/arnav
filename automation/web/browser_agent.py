from playwright.sync_api import sync_playwright
from automation.web.google_agent import GoogleAgent


class BrowserAgent:

    def __init__(self):

        print("BrowserAgent INIT")

        self.playwright = None
        self.browser = None
        self.page = None

        self.google = GoogleAgent(self)

    # Browser Launch
    def ensure_browser(self):

        if self.page is None:

            print("Launching Browser...")

            self.playwright = sync_playwright().start()

            self.browser = self.playwright.chromium.launch(
                headless=False
            )

            self.page = self.browser.new_page()

    # YouTube
    def open_youtube(self):

        self.ensure_browser()

        self.page.goto("https://www.youtube.com")

        self.page.wait_for_load_state()

        return "YouTube opened."

    def youtube_search(self, query):

        self.ensure_browser()

        url = (
            "https://www.youtube.com/results?search_query="
            + query.replace(" ", "+")
        )

        self.page.goto(url)

        self.page.wait_for_load_state()

        return f"Searching {query}."

    def play_first_video(self):

        self.ensure_browser()

        self.page.wait_for_selector(
            "ytd-video-renderer",
            timeout=10000
        )
        
        print("Videos found!")
        self.page.locator(
            "ytd-video-renderer"
        ).first.click()
        
        print("Clicked First Video")
        return "Playing first video."

    # Browser Close
    def close(self):

        if self.browser:

            self.browser.close()

        if self.playwright:

            self.playwright.stop()