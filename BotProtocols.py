from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Surface:

    def __init__(self, browser):
        self.browser = browser

    def like_photos(self, hashtag):
        browser = self.browser
        browser.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        sleep(2)

        pic_refs = []
        #scroll down to load images and gather the hrefs
        for i in range(1,7):
            try:
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
                #get tags
                hrefs_in_view = browser.find_elements_by_tag_name('a')
                #get hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view if '.com/p/' in elem.get_attribute('href')]
                #for every unique picture
                [pic_refs.append(href) for href in hrefs_in_view if href not in pic_refs]
            except Exception:
                print("exception1")
                continue
            
        #like the photos through each hrefs of pictures
        unique_photos = len(pic_refs)
        for pic_href in pic_refs:
            browser.get(pic_href) #go to picture
            sleep(2)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll down
            try:
                sleep(random.randint(2, 4))
                like_button = browser.find_element_by_xpath("//svg[@aria-label='Like']")
                like_button.click() #click like
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos) + " | Sleeping " + str(second))
                    sleep(1)
            except Exception as e:
                print("exception2")
                sleep(2)
            unique_photos -= 1
