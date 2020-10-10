from selenium.webdriver.common.keys import Keys
from BotProtocols import Surface
from Login import LoginProtocols
from selenium import webdriver
from random import randint
from time import sleep
import sys

if __name__ == "__main__":
    
    username = "username"
    password = "password"
    browser = webdriver.Firefox()
    browser.implicitly_wait(5) #if selenium can't find an element, it waits 5 seconds and tries again
    Log = LoginProtocols(browser)
    Log.login(username, password, browser)
    
    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0

    Bot = Surface(browser)
    Bot.like_photos("beauty")

    print("finished")
    
    browser.close()
