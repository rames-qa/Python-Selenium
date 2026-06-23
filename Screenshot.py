from selenium import webdriver

# Launch Chrome
driver = webdriver.Chrome()

# Open website
driver.get("https://www.google.com")

# Take screenshot
driver.save_screenshot("google_screenshot.png")

print("Screenshot captured successfully!")

# Close browser
driver.quit()
