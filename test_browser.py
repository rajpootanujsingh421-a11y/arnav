from automation.web.browser_agent import BrowserAgent

browser = BrowserAgent()

browser.youtube_search(
    "Hanuman Chalisa gym workout"
)

browser.play_first_video()

input()