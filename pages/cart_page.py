from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    #Handles interactions with the cart page on Amazon.

    #Locators
    CART_PRODUCT_TITLE = (By.CSS_SELECTOR, "span.sc-product-title") #Product title in cart
    DELETE_BUTTON = (By.CSS_SELECTOR, "input[data-action= 'delete'][type='submit']") #Delete button for cart item
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "[data-feature-id='delete-success-message']") #Empty cart confirmation
    CART_PAGE_INDICATOR = (By.ID, "sc-active-cart") #Cart page indicators
    HOME_PAGE_LOGO = (By.ID, "nav-logo-sprites") #Amazon home page logo (used for returning)

    def __init__(self, driver):
        #Initialize the cart page with BasePage properties.
        super().__init__(driver)

    def is_on_cart_page(self):
        #Verify that the user is on the cart page
        return self.wait_element_presence(self.CART_PAGE_INDICATOR) is not None

    def is_correct_product_in_cart(self, expected_product_name):
        #Verify that the correct product is present in the cart.
        product_title_element = self.wait_element_presence(self.CART_PRODUCT_TITLE)
        cart_product_name = product_title_element.text.strip()

        self.logger.info(f"Product in the cart: {cart_product_name}")
        self.logger.info(f"Expected product name: {expected_product_name}")

        return cart_product_name.startswith(expected_product_name[:20])

    def delete_product_from_cart(self):
        #Delete the product from the cart
        delete_button = self.wait_element_clicable(self.DELETE_BUTTON)
        delete_button.click()
        self.logger.info("Deleted the product from the cart")

    def is_cart_empty(self):
        #Verify that the cart is empty after deletion
        is_empty = self.wait_element_presence(self.EMPTY_CART_MESSAGE) is not None
        self.logger.info(f"Cart empty verification: {is_empty}")
        return is_empty

    def return_to_homepage(self):
        #Return to the homepage and verify successfully go
        home_logo = self.wait_element_clicable(self.HOME_PAGE_LOGO)
        home_logo.click()
        self.logger.info("Go back to the homepage")

        #Verify that the homepage is loaded
        return self.wait_element_presence(self.HOME_PAGE_LOGO) is not None
