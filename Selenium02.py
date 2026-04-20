from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com")

wait = WebDriverWait(driver, 10)

# Wait and enter email
email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
email.send_keys("rameshkur")

# Wait and enter password
password = wait.until(EC.presence_of_element_located((By.NAME, "pass")))
password.send_keys("ramesh@123")
print("The Enter Facebook successefully")