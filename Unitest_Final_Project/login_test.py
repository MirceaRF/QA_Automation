import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Login(unittest.TestCase):
    USERNAME = (By.XPATH,"//input[@placeholder='Username']")
    PASSWORD = (By.XPATH,"//input[@placeholder='Password']")
    LOGIN_BUTTON =(By.XPATH,"//input[@id='login-button']")
    ERROR_MESSAGE =(By.XPATH,"//form/div/h3[@data-test='error']")
    CLICK_X_ERROR =(By.XPATH,"//h3/button")



    def setUp(self):       # setUp = cuvant cheie care defineste o metoda ce stocheaza instructiuni ce trebuie rulate inainte de fiecare test
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.saucedemo.com/')  # url de start


    def tearDown(self):       # tearDown =  cuvant cheie care defineste o metoda ce stocheaza instructiuni ce trebuie rulate dupa fiecare test
        self.chrome.quit()

    def test_navigate_credentiale_corecte(self):
        self.chrome.find_element(*self.USERNAME).send_keys('standard_user')
        self.chrome.find_element(*self.PASSWORD).send_keys('secret_sauce')
        sleep(2)
        self.chrome.find_element(*self.LOGIN_BUTTON).click()


    def test_navigate_credentiale_gresite_1(self):
        self.chrome.find_element(*self.USERNAME).send_keys('Mircea') #uEpic sadface: Username and password do not match any user in this service
        self.chrome.find_element(*self.PASSWORD).send_keys('parola')
        sleep(2)
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(2)

    def test_navigate_credentiale_gresite_2(self):
        self.chrome.find_element(*self.USERNAME).send_keys('locked_out_user')   #Epic sadface: Sorry, this user has been locked out.
        self.chrome.find_element(*self.PASSWORD).send_keys('secret_sauce')
        sleep(2)
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(2)
    def test_navigate_credentiale_gresite_3(self):
        self.chrome.find_element(*self.USERNAME).send_keys('problem_user')   #Apare aceeasi poza la toate produsele
        self.chrome.find_element(*self.PASSWORD).send_keys('secret_sauce')
        sleep(2)
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(2)
    def test_navigate_credentiale_gresite_4(self):
        self.chrome.find_element(*self.USERNAME).send_keys('performance_glitch_user')   # Pagina fuctioneaza cu intarziere
        self.chrome.find_element(*self.PASSWORD).send_keys('secret_sauce')
        sleep(2)
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(2)

    def test_verificare_mesaj_eroare(self):
        self.test_navigate_credentiale_gresite_1()
        error = self.chrome.find_element(*self.ERROR_MESSAGE)
        sleep(3)
        assert error.is_displayed(),'Mesajul nu este vizibil'
