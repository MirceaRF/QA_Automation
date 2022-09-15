import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Product(unittest.TestCase):
    BACKPACK = (By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
    BIKELIGHT = (By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']")
    TSHIRT = (By.XPATH,"//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    USERNAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    LIST = (By.XPATH,"//*[@id='header_container']/div[2]/div[2]/span/select")
    LIST_AZ = (By.XPATH,"//*[@id='header_container']/div[2]/div[2]/span/select/option[1]")
    LIST_LOHI = (By.XPATH,"//*[@id='header_container']/div[2]/div[2]/span/select/option[3]")


    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.saucedemo.com/inventory.html')
        self.chrome.find_element(*self.USERNAME).send_keys('standard_user')
        self.chrome.find_element(*self.PASSWORD).send_keys('secret_sauce')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()


    def tearDown(self):
        self.chrome.quit()

    def test_add_to_cart(self):
        self.chrome.find_element(*self.BACKPACK).click()
        self.chrome.find_element(*self.BIKELIGHT).click()
        self.chrome.find_element(*self.TSHIRT).click()
        sleep(3)

    def test_list(self):
        self.chrome.find_element(*self.LIST_AZ).click()   #ordonare lista A-Z
        sleep(3)
        self.chrome.find_element(*self.LIST_LOHI).click()  # pret lo-hi
        sleep(3)