import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Page Object Model 
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def is_login_successful(self):
        self.wait.until(EC.url_contains("inventory"))
        return "inventory" in self.driver.current_url
#  Pytest Fixture
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
# ===== Test Data =====
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce")])
def test_multiple_logins(driver, username, password):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login(username, password)

    assert login_page.is_login_successful(), f"Login failed for user: {username}"
# Run without terminal 
if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html", "--self-contained-html"])