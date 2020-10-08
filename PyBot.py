from time import sleep
from selenium import webdriver
import sys

#start browser
browser = webdriver.Firefox()

#go to instagram website
browser.get('https://www.instagram.com/')

sleep(5)

#credentials
username = sys.argv[1]
password = sys.argv[2]



browser.close()
