from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

query = "laptop"
file = 0

# create folder if not exists
os.makedirs("data", exist_ok=True)

for i in range(1, 3):
    driver.get("https://www.amazon.in/s?k=laptop")

    time.sleep(3)

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")

    print(f"{len(elems)} items found")

    for elem in elems:
        d = elem.get_attribute("outerHTML")

        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)

        file += 1
        print(elem.text)

driver.quit()