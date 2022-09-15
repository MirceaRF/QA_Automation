import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Cart(unittest.TestCase):
    CHECKOUT =(By.XPATH,"//*[@id='checkout']")
    USERNAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    BACKPACK = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    BIKELIGHT = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
    TSHIRT = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    SHOPPING_CART = (By.XPATH,"//div[@id='shopping_cart_container']/a")


    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.saucedemo.com/cart.html')
        self.chrome.find_element(*self.USERNAME).send_keys('standard_user')
        self.chrome.find_element(*self.PASSWORD).send_keys('secret_sauce')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(6)


    def tearDown(self):
        self.chrome.quit()

    def test_checkout(self):
        self.chrome.find_element(*self.BACKPACK).click()
        self.chrome.find_element(*self.BIKELIGHT).click()
        self.chrome.find_element(*self.TSHIRT).click()
        sleep(3)
        self.chrome.find_element(*self.SHOPPING_CART).click()
        sleep(3)
        self.chrome.find_element(*self.CHECKOUT).click()