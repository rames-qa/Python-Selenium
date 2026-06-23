import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 1. Set up Chrome Options
options = Options()
options.add_argument("--guest")

# 2. Launch Chrome browser and maximize
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# 3. Define users and password
users = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
]
password = "secret_sauce"

try:
    # 4. Loop through each user
    for user in users:
        driver.get("https://www.saucedemo.com")

        # Locate username textbox, clear it, and enter value
        username_field = driver.find_element(By.ID, "user-name")
        username_field.clear()
        username_field.send_keys(user)

        # Locate password textbox, clear it, and enter value
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)

        # Locate login button and click
        driver.find_element(By.ID, "login-button").click()

        # Pause execution for 2 seconds
        time.sleep(2)

        print(f"Login tried for user: {user}")

        # Navigate back to the login page
        driver.back()

finally:
    # Keeps the browser open just like your commented out //driver.quit(); 
    # But using a try-finally ensures resources can clean up safely later.
    # Uncomment the line below if you want the browser to close automatically at the end.
    # driver.quit()
    pass