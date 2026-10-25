import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login_success(driver, local_server):
    login_page = LoginPage(driver, local_server).open()
    login_page.login("test_user_123@mail.com", "Passw0rd!")
    
    home_page = HomePage(driver)
    assert home_page.is_logged_in(), "Не удалось войти в систему"
    assert login_page.get_message() == "OK"
    driver.save_screenshot("screenshots/login_success.png")

def test_login_wrong_password(driver, local_server):
    login_page = LoginPage(driver, local_server).open()
    login_page.login("test_user_123@mail.com", "wrong_pass")
    
    home_page = HomePage(driver)
    assert not home_page.is_logged_in(), "Система пустила с неверным паролем!"
    assert login_page.get_message() == "Ошибка логина"
    driver.save_screenshot("screenshots/login_error.png")