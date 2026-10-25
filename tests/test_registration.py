import os
import logging
from pages.register_page import RegisterPage

# Доработка: Логирование
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

# Создаем папку для скриншотов, если её нет
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

def test_register_success(driver, index_url):
    logger.info("Старт позитивного теста регистрации")
    page = RegisterPage(driver, index_url).open()
    
    # Передаем ХОРОШИЕ данные
    page.fill_and_submit("test_user_123@mail.com", "Passw0rd!")
    
    msg = page.get_message()
    logger.info(f"Получено сообщение: {msg}")
    
    assert msg == "Успешная регистрация"
    assert page.is_logged_in()
    
    # Скриншот успеха в папку screenshots
    driver.save_screenshot("screenshots/registration_success.png")
    logger.info("Тест пройден, скриншот сохранен")

def test_register_invalid(driver, index_url):
    logger.info("Старт негативного теста (невалидные данные)")
    page = RegisterPage(driver, index_url).open()
    
    # Передаем ПЛОХИЕ данные
    page.fill_and_submit("bad-email", "123")
    
    msg = page.get_message() # ← Теперь тут используется wait, бага не будет
    logger.info(f"Получено сообщение: {msg}")
    
    assert msg == "Ошибка регистрации"
    assert not page.is_logged_in()
        # Скриншот ошибки в папку screenshots
    driver.save_screenshot("screenshots/registration_error.png")
    logger.info("Негативный тест пройден, скриншот сохранен")