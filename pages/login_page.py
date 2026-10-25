from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}/index.html"
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.url)
        return self

    def login(self, email, password):
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "passwd_login").send_keys(password)
        self.driver.find_element(By.ID, "SubmitLogin").click()
        return self

    def get_message(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "loginMsg"))).text