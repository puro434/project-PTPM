from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.url)
        return self

    def fill_and_submit(self, email, password):
        # Вводим email и жмём кнопку
        self.driver.find_element(By.ID, "email_create").send_keys(email)
        self.driver.find_element(By.ID, "SubmitCreate").click()
        
        # Ждём форму и заполняем
        self.wait.until(EC.visibility_of_element_located((By.ID, "customer_firstname"))).send_keys("Ivan")
        self.driver.find_element(By.ID, "customer_lastname").send_keys("Petrov")
        self.driver.find_element(By.ID, "passwd").send_keys(password)
        self.driver.find_element(By.ID, "address1").send_keys("Lenina 1")
        self.driver.find_element(By.ID, "city").send_keys("Moscow")
        self.driver.find_element(By.ID, "postcode").send_keys("101000")
        self.driver.find_element(By.ID, "phone_mobile").send_keys("79990001122")
        
        # Отправляем
        self.driver.find_element(By.ID, "submitAccount").click()
        return self

    def get_message(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "registerMsg"))).text
        
    def is_logged_in(self):
        return "my-account" in self.driver.current_url