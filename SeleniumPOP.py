import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Initialize WebDriver and Maximize Window
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

try:
    # --- 1. Simple Alert ---
    driver.find_element(By.XPATH, "(//a[@data-toggle='tab'])[1]").click()
    driver.find_element(By.XPATH, "//button[@onclick='alertbox()']").click()
    time.sleep(2)
    
    # Switch to alert and accept (Click OK)
    driver.switch_to.alert.accept()

    # --- 2. Confirmation Pop Up ---
    driver.find_element(By.XPATH, "(//a[@data-toggle='tab'])[2]").click()
    driver.find_element(By.XPATH, "//button[@onclick='confirmbox()']").click()
    time.sleep(2)
    
    # Switch to alert and dismiss (Click Cancel)
    driver.switch_to.alert.dismiss()

    # --- 3. Pop Up with Textbox ---
    driver.find_element(By.XPATH, "(//a[@data-toggle='tab'])[3]").click()
    driver.find_element(By.XPATH, "//button[@onclick='promptbox()']").click()
    time.sleep(2)
    
    # Store alert in a variable to perform multiple actions smoothly
    prompt_alert = driver.switch_to.alert
    prompt_alert.send_keys("Ramesh")
    prompt_alert.accept()

    # --- 4. JavaScript Scrolling Loop ---
    # Python's driver has native execute_script support (No casting required)

    # Scroll Down
    for _ in range(10):
        driver.execute_script("window.scrollBy(0,300)")
        time.sleep(0.3)

    # Scroll Up
    for _ in range(10):
        driver.execute_script("window.scrollBy(0,-300)")
        time.sleep(0.3)

    # Scroll Right
    for _ in range(10):
        driver.execute_script("window.scrollBy(300,0)")
        time.sleep(0.3)

    # Scroll Left
    for _ in range(10):
        driver.execute_script("window.scrollBy(-300,0)")
        time.sleep(0.3)

finally:
    # Safely close the browser session
    driver.quit()