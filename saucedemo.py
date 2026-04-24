from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

options = Options()
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    user_input = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    user_input.send_keys("standard_user")
    
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    sort_dropdown_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
    
    dropdown = Select(sort_dropdown_element)
    dropdown.select_by_value("lohi") 
    
    print(f"Current Page= {driver.title}")
    print("Items sorted successfully.")
    
    driver.save_screenshot("saucedemo_results.png")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()