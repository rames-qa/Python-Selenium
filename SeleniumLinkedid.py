from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
options = Options()
options.add_argument("--start-maximized")

# Launch browser
driver = webdriver.Chrome(options=options)

# Wait setup
wait = WebDriverWait(driver, 10)

# Open LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Enter Email
wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("rameshkumarkkannan@gmail.com")

# Enter Password
driver.find_element(By.ID, "password").send_keys("Dhksha.S@695")

# Click Login (ONLY ONCE)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait for successful login (feed page)
wait.until(EC.url_contains("feed"))

print("Login Successful")

# Close browser
driver.quit()