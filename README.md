Amazon Automation Project

📌 Project Overview
This project is an automated testing framework for Amazon.com.tr, built using Selenium WebDriver with Python. It follows the Page Object Model (POM) to ensure modular and reusable test automation.

📂 Project Structure
Bootcamp_Automation_Project/
│-- pages/                   # Page Object Model classes
│   ├── base_page.py         # Base class for common methods
│   ├── home_page.py         # Homepage elements & methods
│   ├── search_results_page.py  # Search results interactions
│   ├── product_page.py      # Product details & cart interactions
│   ├── cart_page.py         # Cart page interactions
│
│-- tests/                   # Test cases
│   ├── test_check_add_to_cart_amazon.py  # Main test scenario
│
│-- .venv/                    # Virtual environment (optional)
│-- requirements.txt           # Python dependencies
│-- README.md                  # Project documentation
│-- .gitignore                 # Files to ignore in Git

🚀 Features Implemented
✅ Automates search functionality for products (e.g., "Samsung")
✅ Navigates through search results and selects a product
✅ Adds selected product to the cart and verifies it
✅ Deletes product from cart and verifies cart is empty
✅ Returns to the homepage after completing the process

⚙️ Technologies Used
Python 🐍
Selenium WebDriver 🌐
PyTest / Unittest ✅
Page Object Model (POM) 🏗️
Logging for Information 📄

Run the test:
python -m unittest tests/test_check_add_to_cart_amazon.py

🔍 Test Scenario
1️⃣ Go to Amazon homepage and accept cookies (if prompted).
2️⃣ Search for a product (e.g., Samsung).
3️⃣ Navigate to the second page of search results.
4️⃣ Select the third product from the results.
5️⃣ Add the product to the cart and verify it is added.
6️⃣ Proceed to the cart page and verify correct product details.
7️⃣ Remove the product from the cart and ensure the cart is empty.
8️⃣ Return to the homepage and confirm successful navigation.
