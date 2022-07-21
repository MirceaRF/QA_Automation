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

# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()
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

#-------------------------------------
#------------● 3 după textul de pe element

# # selector by Xpath - in f de textul vizibil
chrome.find_element(By.XPATH, '//a[text()="Submit"]').click()

chrome.get('http://automationpractice.com/index.php')
#<a data-toggle="tab" href="#homefeatured" class="homefeatured">Popular</a>
chrome.find_element(By.XPATH, '//a[text()="Popular"]').click()
sleep(2)
#<a href="http://automationpractice.com/index.php?controller=contact" title="Contact Us">Contact us</a>
chrome.find_element(By.XPATH, '//a[text()="Contact us"]').click()
sleep(2)
#<a href="http://automationpractice.com/index.php?id_category=3&amp;controller=category" title="Women" class="">Women</a>
chrome.find_element(By.XPATH, '//a[text()="Women"]').click()
sleep(2)

#-------------------------------------

#------------● 1 cu SAU, folosind pipe |

#//*[@id="layered_id_attribute_group_1"]
#//*[@id="layered_id_attribute_group_2"]
#<a href="http://automationpractice.com/index.php?id_category=3&amp;controller=category#">M<span> (7)</span></a>
# # selector by Xpath - OR primul gasit dintre variante  ->  | = sau
s = chrome.find_element(By.XPATH, '//*[@id="layered_id_attribute_group_1"] | //*[@id="layered_id_attribute_group_2"]')

sleep(3)
s.click()
sleep(2)


#-------------------------------------

#------------● 1 cu *

# selector by Xpath - * toate elementele care resecta regula
#  * inseamna un inlocuitor pentru toate elementele care respecta regula

#//*[@id="search_query_top"]
chrome.find_element(By.XPATH, '//*[@id="search_query_top"]').send_keys('REGULA')
sleep(3)

#-----------------
#----------● 1 după parțial text

# selector by Xpath - in f de textul partial + luam textul de pe el cu proprietatea text
chrome.get('https://formy-project.herokuapp.com/form')
sleep(2)
#//a[contains(text(), "key")]
#//*[@id="navbarDropdownMenuLink"]
#<a class="dropdown-item" href="/keypress">Key and Mouse Press</a>
chrome.find_element(By.XPATH, '//a[text()="Butt"]').click()
sleep(3)


#-------------------------------------





#---● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci cu (xpath)[1]

