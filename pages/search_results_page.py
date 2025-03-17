import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResultPage(BasePage):
    #Handles interactions with the search results page on Amazon.

    #Locators
    SEARCH_RESULT = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")
    SECOND_PAGE = (By.XPATH, "//a[contains(@aria-label, '2 sayfasına git')]")
    PAGE_INDICATOR = (By.CSS_SELECTOR, "span.s-pagination-item.s-pagination-selected")
    THIRD_PRODUCT = (By.XPATH, "(//div[@data-component-type='s-search-result'])[3]")
    PRODUCT_TITLE = (By.ID, "productTitle")

    def __init__(self, driver):
        super().__init__(driver) #Initialize homepage using BasePage.
        self.logger = logging

    def check_searched_page(self, search_text):
        products = self.find_element(self.SEARCH_RESULT)
        contains_text = search_text.lower() in products.text.lower()
        self.logger.info(f"Checking search results for '{search_text}': {contains_text}")
        return contains_text

    def go_to_second_page(self):
        # Navigate to the second page of search results.
        second_page_button = self.wait_element_presence(self.SECOND_PAGE)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", second_page_button)
        self.logger.info("Scrolling to the second page button.")

        ActionChains(self.driver).move_to_element(second_page_button).click().perform()
        self.logger.info("Clicked on the second page button.")

        #Wait for the page to update
        self.wait_element_presence(self.PAGE_INDICATOR)

    def is_on_second_page(self):
        #Verify that the user is on the second page by checking the page indicator.
        page_number = self.wait_element_presence(self.PAGE_INDICATOR).text
        self.logger.info(f"Found page number indicator: {page_number}")
        return page_number == "2"

    def select_third_prduct(self):
        #Select and click the third product from the search results.
        third_product = self.wait_element_visible(self.THIRD_PRODUCT)
        self.driver.execute_script("arguments[0].scrollIntoView();", third_product)
        self.logger.info("Scrolled to the third product.")

        ActionChains(self.driver).move_to_element(third_product).click().perform()
        self.logger.info("Clicked on the third product.")

    def is_on_third_product_page(self, search_text):
        #Verify that the opened product contains the searched text.
        product_title = self.wait_element_visible(self.PRODUCT_TITLE).text
        contains_text = search_text.lower() in product_title.lower()
        self.logger.info(f"Opened product title: {product_title}, contains '{search_text}': {contains_text}")
        return contains_text
