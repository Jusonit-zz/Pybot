from time import sleep

class Surface:

    def __init__(self, browser):
        self.browser = browser

    def like_photos(self, hashtag):
        browser = self.browser
        browser.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        sleep(2)
