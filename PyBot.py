from time import sleep
from selenium import webdriver
import sys

#credentials from command line arguments, or manually edit here if preferred
username = sys.argv[1]
password = sys.argv[2]

#start browser
browser = webdriver.Firefox()

#sets five seconds of waiting time
#if selenium can't find an element, it waits 5 seconds and tries again
browser.implicitly_wait(5)

#types url on the address bar and hits enter
browser.get('https://www.instagram.com/')

#to let page load
sleep(2)

#finds username and password inputs by css
username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

#types your username and password.
username_input.send_keys(username)
password_input.send_keys(password)
#or if manually adding it here
#username_input.send_keys("your_username")
#password_input.send_keys("your_password")

sleep(2)

#finds the login button and clicks
login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(5)

browser.close()
