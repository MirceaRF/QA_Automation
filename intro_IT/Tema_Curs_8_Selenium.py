# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)


chrome.maximize_window() # este o metoda folosita pentru maximizarea browserului
'''
Exerciții obligatorii - grad de dificultate: Usor spre Mediu
Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
'''

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form') # metoda get este o metoda prin care putem naviga la un anumit link

#--------selector by ID-----------
#  id="first-name"


first_name = chrome.find_element(By.ID,"first-name")
sleep(1)
first_name.send_keys('Floroaie')
sleep(1)

# id="last-name"

last_name = chrome.find_element(By.ID,"last-name")
sleep(1)
last_name.send_keys('Mircea')
sleep(1)

# id="autocomplete"
# selector by Link Text
chrome.get('https://formy-project.herokuapp.com/')
sleep(2)
chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()  # selector by Link Text
sleep(2)
#chrome.get('https://formy-project.herokuapp.com/autocomplete')

autocomplete = chrome.find_element(By.ID,"autocomplete")  # id="autocomplete"
sleep(2)
autocomplete.send_keys('Aleea-Baita')
sleep(2)

#------------● Link text---------

# selector by Link Text
chrome.get('https://formy-project.herokuapp.com/')
sleep(2)
chrome.find_element(By.LINK_TEXT, 'Buttons').click()
sleep(2)
chrome.get('https://formy-project.herokuapp.com/')
sleep(2)
chrome.find_element(By.LINK_TEXT, 'Checkbox').click()
sleep(2)

#-----------● Parțial link text-----------
chrome.get('https://formy-project.herokuapp.com/')
sleep(2)
# selector by Partial Link Text
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Enab').click()
sleep(2)
chrome.get('https://formy-project.herokuapp.com/')
sleep(2)
# selector by Partial Link Text
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Page').click()
sleep(2)

chrome.get('https://formy-project.herokuapp.com/')
sleep(2)
# selector by Partial Link Text
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Radio').click()
sleep(2)

#-------------● Name------------

#<input type="text" class="is_required validate account_input form-control" data-validate="isEmail" id="email_create" name="email_create" value="">

chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
sleep(2)

# selector by Name
chrome.find_element(By.NAME, "email_create").send_keys('Mirceaf@gmail.com')
sleep(2)
#<input class="is_required validate account_input form-control" data-validate="isEmail" type="text" id="email" name="email" value="">
chrome.find_element(By.NAME, "email").send_keys('Mirceaf@gmail.com')
sleep(2)

# <input class="is_required validate account_input form-control" type="password" data-validate="isPasswd" id="passwd" name="passwd" value="">
chrome.find_element(By.NAME, "passwd").send_keys('1234')
sleep(2)

#------------● Tag*-----------
chrome.get('https://formy-project.herokuapp.com/form')

# selector by Tag
chrome.find_element(By.TAG_NAME, 'input')

sleep(3)

# gasim mai multe si le punem in lista
lista_taguri = chrome.find_elements(By.TAG_NAME, 'input') # am definit o lista care sa stocheze toate elementele de pe site identificabile prin tag-ul de input
lista_taguri[0].send_keys('Floroaie')
lista_taguri[1].send_keys('Mircea')
lista_taguri[2].send_keys('Tester')
lista_taguri[3].click()
print(len(lista_taguri))

sleep(3)

#--------------● Class name*------------
chrome.find_element(By.CLASS_NAME, 'form-control').send_keys('Test')

# gasim mai multe si punem in lista
lista_elemente = chrome.find_elements(By.CLASS_NAME, 'form-control')
lista_elemente[1].send_keys("Test")
lista_elemente[3].send_keys("1")

sleep(3)

#-------------● Css-----------------

# selector by CSS - ID

chrome.get('http://automationpractice.com/index.php?controller=contact')
##email
#<input class="form-control grey validate" type="text" id="email" name="from" data-validate="isEmail" value="">
chrome.find_element(By.CSS_SELECTOR, 'input#email').send_keys('Mircea@gmail.com') # # = identificator pentru id
sleep(2)

# selector by CSS - Class - only first one of multiple matches
chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
##id_order
#id_order    <input class="form-control grey" type="text" name="id_order" id="id_order" value="">
###login_form > div > div.form-group.form-error
#<input class="is_required validate account_input form-control" data-validate="isEmail" type="text" id="email" name="email" value="">

chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('Apare sus la Search')
sleep(3)

# selector by CSS - atribut=valoare
# [] = identificator pentru atribut = valoare
#id="email_create" name="email_create" value="">
chrome.find_element(By.CSS_SELECTOR, 'input[id="email_create"]').send_keys('Mircea@gmail.com')
sleep(2)

''''
Pentru xpath identifică elemente după criteriile de mai jos:
● 3 după atribut valoare
● 3 după textul de pe element
● 1 după parțial text
● 1 cu SAU, folosind pipe |
● 1 cu *
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]
● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
ce element vreau să interacționez.

'''
#--------------Xpath------------
# Atribut  valoare

chrome.get('https://formy-project.herokuapp.com/form')

#//*[@id="first-name"]
#//*[@id="last-name"]
#//*[@id="job-title"]
chrome.find_element(By.XPATH, '//input[@id="first-name"]').send_keys("Mircea")
sleep(3)
chrome.find_element(By.XPATH, '//input[@id="last-name"]').send_keys("Floroaie")
sleep(3)
chrome.find_element(By.XPATH, '//input[@id="job-title"]').send_keys("Tester")
sleep(3)

#● 3 după textul de pe element