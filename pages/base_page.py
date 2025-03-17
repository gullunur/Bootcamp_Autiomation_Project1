import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    #Base class for all pages that provides common functionalities.

    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)

    def __init__(self, driver):
        #Initialize the driver and explicit wait instance.
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.logger = logging.getLogger(__name__)  #Define logger for each page

    def find_element(self, locator):
        #Find an element using the given locator.
        self.logger.info(f"Finding element: {locator}")
        return self.driver.find_element(*locator)

    def get_current_url(self, get_current_url):
        #Go to the given URL
        self.logger.info(f"Got to URL: {get_current_url}")
        self.driver.get(get_current_url)

    def get_titles(self):
        #Get the current page title.
        title = self.driver.title
        self.logger.info(f"Current Page Title: {title}")
        return title

    def click_element(self, locator):
        #Click an element using the given locator.
        self.logger.info(f"Clicking element: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def wait_element_clicable(self, locator):
        #Wait until the element is clickable and return it.
        self.logger.info(f"Waiting for element to be clickable: {locator}")
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_element_visible(self, locator):
        #Wait until the element is visible on the page and return it.
        self.logger.info(f"Waiting for element to be visible: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_element_presence(self, locator):
        #Wait until the element is present in the DOM (but not nesessarily visible).
        self.logger.info(f"Waiting for element presence: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))
