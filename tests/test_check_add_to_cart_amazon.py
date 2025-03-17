import unittest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.search_results_page import SearchResultPage


class TestCheckAddToCardAmazon(unittest.TestCase):
    #Amazon automation test suite to validate product search, add to cart, and deletion.

    def setUp(self):
        #Set up the WebDriver instance before each test.
        chrome_options = Options()
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()
        self.driver.get('https://www.amazon.com.tr/')
        self.logger = logging.getLogger(__name__) #Get Logger instance
        self.search_text = "Samsung"

    def test_check_add_to_cart_amazon(self):
        #Test case for searching, adding to cart, verifying and deleting a product.


        # 1. Go to the home page
        home_page = HomePage(self.driver)
        home_page.get_current_url("https://www.amazon.com.tr/")
        self.assertTrue(home_page.check_homepage_title(), "This is not homepage! The main page should be Amazon.")
        self.logger.info("Go to the home page and verified title")

        # 2.Accept the cookies
        home_page.accept_cookies()
        self.logger.info("Accepted cookies.")

        # 3. Search for the product and verify search results
        home_page.search_for_product(self.search_text)
        search_result_page = SearchResultPage(self.driver)
        self.assertTrue(search_result_page.check_searched_page(self.search_text), "This is not Samsung page!")
        self.logger.info(f"Searched for '{self.search_text}' and verified results.")

        # 4. Go to the second page of search results
        search_result_page.go_to_second_page()
        self.assertTrue(search_result_page.is_on_second_page(), "Not on the second page!")
        self.logger.info("Go to the second page.")

        # 5. Select the third product in the search results
        search_result_page.select_third_prduct()
        self.assertTrue(search_result_page.is_on_third_product_page(self.search_text), "This is not the correct product page!")
        self.logger.info("Selected the third product and verified the product page")

        # 6. Get the product name before adding to cart
        product_page = ProductPage(self.driver)
        selected_product_name = product_page.get_product_name()  # Get the full name of the product
        self.assertIsNotNone(selected_product_name, "Could not retrieve product name!")
        self.logger.info(f"Retrieved product name: {selected_product_name}")

        # 7. Add the product to the cart and verify
        product_page.add_to_cart()
        self.assertTrue(product_page.is_product_added_to_cart(), "Product was not added to the cart!")
        self.logger.info("Product added to cart successfully.")

        # 8. Go to the cart page
        product_page.go_to_cart()
        current_url = self.driver.current_url
        self.assertIn("cart", current_url, "You are not on the cart page!")
        self.logger.info("Go to the cart page.")

        # 9. Verify that the correct product is in the cart
        cart_page = CartPage(self.driver)
        self.assertTrue(cart_page.is_on_cart_page(), "You are not on the cart page!")

        # Check that the product name in the cart matches the name on the product detail page exactly
        product_in_cart = cart_page.is_correct_product_in_cart(selected_product_name)
        self.logger.info(f"Cart product verification result: {product_in_cart}")
        self.assertTrue(product_in_cart, "The correct product is not in the cart!")
        self.logger.info("Verified that the correct product is in the cart.")

        # 10. Delete the product from the cart and verify
        cart_page.delete_product_from_cart()
        is_empty = cart_page.is_cart_empty()
        self.logger.info(f"Cart empty verification results: {is_empty}")
        self.assertTrue(is_empty, "The cart is not empty after deletion!")
        self.logger.info("Verified that the cart is empty after deletion.")

        # 11. Return to the homepage and verify
        on_homepage = cart_page.return_to_homepage()
        self.logger.info(f"Homepage verification result: {on_homepage}")
        self.assertTrue(on_homepage, "You are not on the homepage!")
        self.logger.info("Successfully returned to the homepage.")


    def tearDown(self):
        #Quit the WebDriver instance after each test.
        self.driver.quit()
        self.logger.info("Test execution completed. WebDriver instance closed.")

if __name__ == '__main__':
    unittest.main()

