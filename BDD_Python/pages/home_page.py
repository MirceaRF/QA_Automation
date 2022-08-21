from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import Base_page


class Home_page(Base_page):
    SEARCH_TEXT_BOX = (By.ID, "gh-ac")
    SEARCH_BUTTON   = (By.ID, "gh-btn")
    SEARCH_RESULTS  = (By.XPATH, '//h1/span[@class="BOLD"]')


    def set_product_search(self):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys("Iphone")
        sleep(2)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        sleep(2)

    def check_search_results(self):
        result_list = self.chrome.find_elements(*self.SEARCH_RESULTS)
        resultat_final=result_list[0].text.replace(',', '')
        assert int(resultat_final) >= 2
        sleep(2)

    def navigate_to_home_page(self):
        self.chrome.get('https://www.ebay.com/')
        sleep(2)






