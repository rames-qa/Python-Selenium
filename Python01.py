from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

# Wait for title
WebDriverWait(driver, 10).until(EC.title_contains("Swag Labs"))

# Wait for username field
username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "user-name"))
)

password = driver.find_element(By.ID, "password")

# Enter login details
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# Click login
driver.find_element(By.ID, "login-button").click()

# Wait for next page (inventory)
WebDriverWait(driver, 10).until(
    EC.url_contains("inventory")
)

print("Login Successful ✅")

driver.quit()