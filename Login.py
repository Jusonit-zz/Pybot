from time import sleep

class LoginProtocols:
    def __init__(self, browser):
        self.browser = browser
        browser.get('https://www.instagram.com/')
        sleep(2)

    def login(self, username, password, browser):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)
    
