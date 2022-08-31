from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import unittest
from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import unittest  #  importarea librariei unit test care va face programul grupat in bucati rulabile individual
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#https://pypi.org/project/webdriver-manager/

class WebForm(unittest.TestCase):
    FIRST_NAME = (By.XPATH , "//input[@id='first-name']")
    LAST_NAME = (By.XPATH,"//input[@id='last-name']")
    JOB_TITLE =(By.XPATH,"//input[@id='job-title']")
    EDUCATION = (By.XPATH,"//input[@id='radio-button-1']")
    GEN = (By.XPATH,"//input[@id='checkbox-1']")
    #//option[2]
    EXPERIENCE =(By.XPATH,"//option[2]")
    DATE = (By.XPATH,"//input[@id='datepicker']")
    DATE_PICK =(By.XPATH,"//tr/td[@class='today day']")
    SUBMIT = (By.XPATH,"//a[text()='Submit']")

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get('https://formy-project.herokuapp.com/form')
        self.driver.maximize_window()
        sleep(5)

    def tearDown(self):
        sleep(5)
        self.driver.quit()
    def test_complet(self):
        self.driver.find_element(*self.FIRST_NAME).send_keys('Mircea')
        self.driver.find_element(*self.LAST_NAME).send_keys('Floroaie')
        self.driver.find_element(*self.JOB_TITLE).send_keys('Tester')
        self.driver.find_element(*self.EDUCATION).click()
        self.driver.find_element(*self.GEN).click()
        self.driver.find_element(*self.EXPERIENCE).click()
        self.driver.find_element(*self.DATE).click()
        self.driver.find_element(*self.DATE_PICK).click()
        self.driver.find_element(*self.SUBMIT).click()

    def test_submit(self):
        button=self.driver.find_element(*self.SUBMIT)
        assert button.is_displayed(),' The button is not displayed'









