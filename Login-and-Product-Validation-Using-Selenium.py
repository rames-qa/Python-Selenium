from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Create browser options
options = Options()
options.add_argument("--guest")   # guest mode

# Launch browser with options
driver = webdriver.Chrome(options=options)

try:
    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # Get all product names
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    print(f"Total products: {len(products)}\n")

    # Print product names
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product.text}")

    time.sleep(3)

finally:
    driver.quit()