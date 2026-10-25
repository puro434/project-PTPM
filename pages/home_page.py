class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def is_logged_in(self):
        # Проверяем, что в URL появился хэш #my-account
        return "my-account" in self.driver.current_url

    def get_current_url(self):
        return self.driver.current_url