from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_page import Base_page


class Home_page(Base_page):
    USERNAME = (By.XPATH, "//input[@id='username']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='radius']")

    def navigate_to_home_page(self):
        self.chrome.get('https://the-internet.herokuapp.com/login')

    def complete_username_password(self,username="",password=""):
        self.chrome.find_element(*self.USERNAME).send_keys(username)
        self.chrome.find_element(*self.PASSWORD).send_keys(password)
        sleep(3)

    def click_login_button(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(3)
