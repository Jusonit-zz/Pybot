from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import random

class Surface:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5) #if selenium can't find an element, it waits 5 seconds and tries again

    def openPage(self):
        browser = self.browser
        browser.get('https://www.instagram.com/')
        sleep(2)

    def login(self):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        errors = self.browser.find_elements_by_css_selector('#error_message')
        assert len(errors) == 0
        
        sleep(2)

    def like_photos(self, hashtag, comment_list):
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
                like_button = browser.find_element_by_class_name('fr66n') # the like button
                like_button.click() #click like
                self.type_comments(comment_list)
                for second in reversed(range(0, random.randint(1, 3))):
                    print("#" + hashtag + ': unique photos left: ' + str(unique_photos) + " | Sleeping " + str(second))
                    sleep(1)
            except Exception as e:
                sleep(2)
            unique_photos -= 1
            
    def type_comments(self, comment_list):
        #comments in 1/5 chance
        chance = random.randint(1,5)
        
        if chance == 5:
            comment = ( 
                comment_list[0][random.randint(0, 2)] + " " +
                comment_list[1][random.randint(0, 4)] + " " +
                comment_list[2][random.randint(0, 3)] + " " +
                comment_list[3][random.randint(0, 25)] + " " +
                comment_list[4][random.randint(0, 5)] 
                   )
            commentArea = self.browser.find_element_by_class_name('Ypffh')
            commentArea.click()
            commentArea = self.browser.find_element_by_class_name('Ypffh')
            commentArea.send_keys(comment)
        

    def closeBrowser(self):
        self.browser.close()
    
        
