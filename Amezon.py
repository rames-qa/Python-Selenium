from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open Amazon
driver.get("https://www.amazon.in")
driver.maximize_window()

# Search for a phone
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Samsung Mobile Phone")
search_box.send_keys(Keys.ENTER)

time.sleep(5)

print("Phone search completed successfully!")

# Close browser
driver.quit()
