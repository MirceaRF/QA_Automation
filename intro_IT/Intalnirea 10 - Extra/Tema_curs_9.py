'''
Implementează o clasă Login care să moștenească unittest.TestCase
Gasește elementele în partea de sus folosind ce selectors dorești:
- setUp()
- Driver
https://the-internet.herokuapp.com/
Click pe Form Authentication
tearDown()
Quit browser

● Test 1
- Verifică dacă noul url e corect

● Test 2
- Verifică dacă page title e corect
● Test 3
- Verifică textul de pe elementul xpath=//h2 e corect
● Test 4
- Verifică dacă butonul de login este displayed

● Test 5
- Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

● Test 6
- Lasă goale user și pass
- Click login
- Verifică dacă eroarea e displayed
● Test 7
- Completează cu user și pass invalide
- Click login
- Verifică dacă mesajul de pe eroare e corect
- Este și un x pus acolo extra așa că vom folosi soluția de mai jos
expected = 'Your username is invalid!'
self.assertTrue(expected in actual, 'Error message text is
incorrect')
● Test 8
- Lasă goale user și pass
- Click login
- Apasă x la eroare
- Verifică dacă eroarea a dispărut
● Test 9
- Ia ca o listă toate //label
- Verifică textul ca textul de pe ele să fie cel așteptat (Username și
Password)
- Aici e ok să avem 2 asserturi

● Test 10
- Completează cu user și pass valide
- Click login
- Verifică ca noul url CONTINE /secure
- Folosește un explicit wait pentru elementul cu clasa ’flash succes’
- Verifică dacă elementul cu clasa=’flash succes’ este displayed

- Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
● Test 11
- Completează cu user și pass valide
- Click login
- Click logout
- Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

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



class Login(unittest.TestCase):
    FORM_AUTENTIFICATION =(By.XPATH, "//a[@href='/login']")
    LOGIN_PAGE =(By.XPATH,"//h2")
    BUTTON_LOGIN =(By.XPATH,"//button/i")
    CHECK_ATTRIBUT_HREF = (By.XPATH,"//a[@href='http://elementalselenium.com/']")
    CLICK_ERROR = (By.XPATH,"//div[@id='flash']")
    USER_NAME =(By.XPATH,"//input[@id='username']")
    PASSWORD = (By.XPATH,"//input[@id='password']")
    CLICK_X = (By.XPATH,"//a[@class='close']")
    LABEL_USER = (By.XPATH,"//label[text()='Username']")
    LABEL_PASS = (By.XPATH,"//label[text()='Password']")
    ELEMENT_CLASS_FLASH_SUCCESS = (By.XPATH,"//div[@class='flash success']")
    LOGOUT=(By.XPATH,"//a[@class='button secondary radius']")




    def setUp(self): #  setUp = cuvant cheie care defineste o metoda ce stocheaza instructiuni ce trebuie rulate inainte de fiecare test
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/') #url de start
        self.chrome.find_element(*self.FORM_AUTENTIFICATION).click()

    def tearDown(self): # tearDown =  cuvant cheie care defineste o metoda ce stocheaza instructiuni ce trebuie rulate dupa fiecare test
        self.chrome.quit()


#Test_1 - Verifică dacă noul url e corect
    #@unittest.skip
    def test_url(self):
        self.chrome.implicitly_wait(10)
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')

#● Test 2- Verifică dacă page title e corect

    def test_page_title(self):
        actual = self.chrome.title
        expected = 'The Internet'   #//*[@id="content"]/div/h2'#<h2>Login Page</h2>
        self.assertEqual(expected, actual, 'Page title is incorrect')
        print(actual)

#Test 3 - Verifică textul de pe elementul xpath=//h2 e corect

    def test_page_text(self):
        actual = self.chrome.find_element(*self.LOGIN_PAGE).text
        expected = 'Login Page'
        self.assertEqual(expected, actual, 'Page text is incorrect')
        print(f'{actual} {expected}')

#Test 4 - Verifică dacă butonul de login este displayed

    def test_button_login(self):
       button = self.chrome.find_element(*self.BUTTON_LOGIN)
       #assert button.is_displayed(), 'the button is not displayed'
       self.assertTrue(button.is_displayed(),'the button is not displayed')
       print(button)

#Test 5 - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

#<a target="_blank" href="http://elementalselenium.com/">Elemental Selenium</a>

    def test_check_attribut(self):
        href = self.chrome.find_element(*self.CHECK_ATTRIBUT_HREF).get_attribute('href')
        assert href =="http://elementalselenium.com/" ,'The href is incorrect'
        print(href)

#Test 6- Lasă goale user și pass - Click login - Verifică dacă eroarea e displayed

    def test_click_login(self):
        self.chrome.find_element(*self.BUTTON_LOGIN).click()
        error = self.chrome.find_element(*self.CLICK_ERROR)
        assert error.is_displayed(),'The error is not visible'
        print(error)


#Test 7
#'''- Completează cu user și pass invalide
#- Click login
#- Verifică dacă mesajul de pe eroare e corect
#- Este și un x pus acolo extra așa că vom folosi soluția de mai jos
#expected = 'Your username is invalid!'
#self.assertTrue(expected in actual, 'Error message text is
#incorrect')'''

    def test_user_pass_invalid(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('Mircea')
        self.chrome.find_element(*self.PASSWORD).send_keys('parola')
        self.chrome.find_element(*self.BUTTON_LOGIN).click()
        error = self.chrome.find_element(*self.CLICK_ERROR)
        self.assertTrue(error.is_displayed()),'the text is not displayed'
        print(error)

#Test 8
#- Lasă goale user și pass - Click login - Apasă x la eroare - Verifică dacă eroarea a dispărut

    def test_click_x(self):
        self.chrome.find_element(*self.BUTTON_LOGIN).click()
        self.chrome.find_element(*self.CLICK_X).click()
        actual_error =self.chrome.find_element(*self.CLICK_ERROR).text
       # print(actual_error)
        assert actual_error != 'Your username is invalid!','Your user name is invalid'

#  Test 9
# - Ia ca o listă toate //label
# - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
# Password)
# - Aici e ok să avem 2 asserturi

    def test_check_text_user_pass(self):
        user = self.chrome.find_element(*self.LABEL_USER).text
        assert user=='Username','Label user incorrect'
        pasw =self.chrome.find_element(*self.LABEL_PASS).text
        assert  pasw=='Password','Label pass incorrect'

#Test 10
#- Completează cu user și pass valide
#- Click login
#- Verifică ca noul url CONTINE /secure
#- Folosește un explicit wait pentru elementul cu clasa ’flash succes’
#- Verifică dacă elementul cu clasa=’flash succes’ este displayed

    def test_completes_user_pass_valide(self):
        self.chrome.find_element(*self.USER_NAME).send_keys("tomsmith")
        self.chrome.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.BUTTON_LOGIN).click()

        try:
            WebDriverWait(self.chrome, 5).until(EC.url_contains('/secure'))
            print("The url contains the keyword '/secure' ")
        except TimeoutException:
            self.assertTrue(False, 'The url is incorrect!')

        WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located(self.ELEMENT_CLASS_FLASH_SUCCESS))
        element = self.chrome.find_element(*self.ELEMENT_CLASS_FLASH_SUCCESS)
        assert element.is_displayed(), f'The element is not displayed!'

        element = self.chrome.find_element(*self.ELEMENT_CLASS_FLASH_SUCCESS).text
        text = "secure area!"
        print(element)
        assert text in element, f'The text {element} does not contains: {text}'


#Test 11  - Completează cu user și pass valide - Click login - Click logout - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

    def test_login_logout(self):
        self.chrome.find_element(*self.USER_NAME).send_keys("tomsmith")
        self.chrome.find_element(*self.PASSWORD).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.BUTTON_LOGIN).click()
        self.chrome.find_element(*self.LOGOUT).click()
        expected = 'https://the-internet.herokuapp.com/login'
        actual = self.chrome.current_url
        self.assertEqual(actual,expected), f'The url {actual} is not equal with the url {expected}'

#Test 12 - brute force password hacking
#- Completează user tomsmith
#- Găsește elementul //h4
#- Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o potențială parolă.
#- Folosește o structură iterativă prin care să introduci rând pe rând parolele și să apeși pe login.
#- La final testul trebuie să îmi printeze fie
#‘Nu am reușit să găsesc parola’
#‘Parola secretă este [parola]’

    def test_brute_force_password_hacking(self):
        first_url, last_url, the_brute_force_password = '   '
        possible_passwords = ['Enter', 'tomsmith', 'for', 'the', 'username', 'and', 'SuperSecretPassword!', 'for',
                              'the', 'password.']
        for i in possible_passwords:
            self.chrome.find_element(*self.USER_NAME).send_keys("tomsmith")
            first_url = self.chrome.current_url
            self.chrome.find_element(*self.PASSWORD).send_keys(i)
            sleep(2)
            self.chrome.find_element(*self.BUTTON_LOGIN).click()
            sleep(2)
            last_url = self.chrome.current_url
            sleep(2)
            if last_url != first_url:
                the_brute_force_password = i
                break
                print(i)
        assert first_url != last_url, 'I do not succeed the password!'
        print(f'I succeed to find the password, it is: "{the_brute_force_password}"')



