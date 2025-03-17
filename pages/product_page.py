from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    #Handles interactions with the product page on Amazon.

    #Locators
    PRODUCT_TITLE = (By.ID, "productTitle") #Product title locators
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button") #Addto cart button locators
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-csa-c-content-id='sw-gtc_CONTENT']") #Go to cart button locator
    CART_ICON = (By.ID, "nav-cart-count") #Cart item count indicator


    def __init__(self, driver):
        # Initialize the product page with BasePage properties.
        super().__init__(driver)

    def get_product_name(self):
        #Retrieve the product name from the product page.
        product_title = self.wait_element_presence(self.PRODUCT_TITLE).text.strip()
        self.logger.info(f"Selected product name: {product_title}")
        return product_title

    def add_to_cart(self):
        add_to_cart_button = self.wait_element_presence(self.ADD_TO_CART_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)
        self.logger.info("Scrolled to the 'Add to Cart' button.")

        self.wait_element_clicable(self.ADD_TO_CART_BUTTON).click()
        self.logger.info("Clicked on the 'Add to Cart' button.")

    def go_to_cart(self):
        #Go to the cart page.
        go_to_cart_button = self.wait_element_clicable(self.GO_TO_CART_BUTTON)
        go_to_cart_button.click()
        self.logger.info("Go to the cart page.")

    def is_product_added_to_cart(self):
        #Verify if the product has been successfully added to the cart.
        cart_count = self.wait_element_visible(self.CART_ICON).text
        self.logger.info(f"Number of products in the cart: {cart_count}")
        return int(cart_count) > 0
