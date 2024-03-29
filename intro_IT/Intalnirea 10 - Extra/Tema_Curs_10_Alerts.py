'''
Tema 10 - VERIFICARI EXTRA
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 9 și ia notițe în caz că ți-a scăpat ceva.
Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
1. Faceti o suita care sa contina testele voastre de la tema 9 + testele de la
intalnirea 10 (care au clasa). Generati raportul
2. Ganditi voi o clasa de test din paginile sugerate in tema 8
- Scrieti cel putin 3 functii de test intr-o clasa (cum am facut la clasa)
Folositi firefox in loc de chrome (ce doriti voi, cate functii de test doriti,
freestyle ca sa incepeti sa ganditi si singuri niste scenarii de test).
Bine de stiut: o functie de test este echivalentul unui test case
Mai multe aici:
https://www.tutorialspoint.com/software_testing_dictionary/test_case.htm

https://www.phptravels.net/
http://automationpractice.com/index.php
https://formy-project.herokuapp.com/
https://the-internet.herokuapp.com/
https://www.techlistic.com/p/selenium-practice-form.html
Sau puteti alege voi ce pagina doriti


'''


import unittest  #  importarea librariei unit test care va face programul grupat in bucati rulabile individual
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Alerts(unittest.TestCase):
    ALERT = (By.XPATH, '//button[text()="Click for JS Alert"]')
    CONFIRM = (By.XPATH, '//button[text()="Click for JS Confirm"]')
    PROMPT = (By.XPATH, '//button[text()="Click for JS Prompt"]')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")

    def tearDown(self) -> None:
        self.chrome.quit()

    # @unittest.skip
    def test_alert(self):
        self.chrome.find_element(*self.ALERT).click()
        sleep(2)
        obj = self.chrome.switch_to.alert  # Ne-am mutat de pe fereastra "https://the-internet.herokuapp.com/javascript_alerts" pe fereastrade alerta
                                                #  si am salvat fereastra de alerta intr-o variabila obj
        print("Alert shows following message: " + obj.text) # Metoda text extrage textul dintr-un element
        # use the accept() method to accept the alert
        sleep(2)
        obj.accept() # metoda accept reprezinta echivalentul clickului pe butonul "OK" din alerta
        print("Clicked on the OK Button in the Alert Window")
        sleep(2)

    #@unittest.skip
    def test_confirm_ok(self):
        self.chrome.find_element(*self.CONFIRM).click()
        obj = self.chrome.switch_to.alert
        # Retrieve the message on the Confirm window
        print(f"Alert shows following message: {obj.text}" )
        sleep(3)
        # use the accept() method to accept the Confirm
        obj.accept()
        print("Clicked on the OK Button in the Confirm Window")
        sleep(3)

    #@unittest.skip
    def test_confirm_cancel(self):
        self.chrome.find_element(*self.CONFIRM).click()
        # Switch the control to the Confirm window
        obj = self.chrome.switch_to.alert
        # Retrieve the message on the Confirm window
        print("Confirm shows following message: " + obj.text)
        sleep(3)
        # use the dismiss() method to cancel the Confirm
        obj.dismiss() # metoda dismiss este echivalentul butonului de "Cancel" din alerta
        print("Clicked on the Cancel Button in the Confirm Window")
        sleep(3)

    #@unittest.skip   # decorator care instruieste sistemul sa nu execute anumite teste
    def test_prompt(self):
        self.chrome.find_element(*self.PROMPT).click()
        sleep(2)
        # Switch the control to the Prompt window
        obj = self.chrome.switch_to.alert
        # Retrieve the message on the Prompt window
        print("Prompt shows following message: " + obj.text)
        # Enter text into the Prompt using send_keys()
        obj.send_keys('Mircea')
        # use the accept() method to accept the Prompt
        obj.accept()
        print("Clicked on the OK Button in the Prompt Window")
        sleep(3)
