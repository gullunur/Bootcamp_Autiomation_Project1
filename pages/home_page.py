from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    #Lacators
    SEARCH_BOX = (By.ID, "twotabsearchtextbox") #Amazon search bar
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button") #Amazon search button
    COOKIE_ACCEPT_BUTTON = (By.ID, "sp-cc-accept") #Accept cookies button
    COOKIE_REJECT_BUTTON = (By.ID, "sp-cc-rejectall-link") #Reject cookies button

    expected_title = "Amazon.com.tr: Elektronik, bilgisayar, akıllı telefon, kitap, oyuncak, yapı market, ev, mutfak, oyun konsolları ürünleri ve daha fazlası için internet alışveriş sitesi"

    def __init__(self, driver):
        super().__init__(driver) #Initialize homepage using BasePage.

    def check_homepage_title(self):
        #Verify that the homepage title is correct.
        result = self.expected_title in self.get_titles()
        self.logger.info(f"Checking homepage title: {result}")
        return result

    def accept_cookies(self):
        try:
            self.logger.info("Attempting to accept cookie.")
            button = self.wait_element_clicable(self.COOKIE_ACCEPT_BUTTON)
            button.click()
        except:
            self.logger.warning("Cookies accept button not found")

    def search_for_product(self, product_name):
        #Search for a product using the search box.
        self.logger.info(f"Searching for product: {product_name}")
        search_box = self.find_element(self.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(product_name)
        self.click_element(self.SEARCH_BUTTON)