import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_implicit_wait(driver, index_url):
    """Тест с неявным ожиданием (implicitly_wait)."""
    driver.implicitly_wait(10) # Ждем до 10 секунд при поиске элемента
    driver.get(index_url)
    
    driver.find_element(By.CSS_SELECTOR, "#start button").click()
    
    start_time = time.time()
    # Неявное ожидание найдет элемент, но нам нужно дождаться, пока JS вставит в него текст
    el = driver.find_element(By.CSS_SELECTOR, "#finish h4")
    
    # Принудительно ждем 3 секунды, так как неявное ожидание не ждет текста
    time.sleep(3) 
    el = driver.find_element(By.CSS_SELECTOR, "#finish h4") # Ищем заново
    elapsed = time.time() - start_time
    
    assert el.text == "Hello World!"
    print(f"\n[Implicit Wait] Элемент найден и текст получен за {elapsed:.2f} сек.")

def test_explicit_wait(driver, index_url):
    """Тест с явным ожиданием (WebDriverWait)."""
    wait = WebDriverWait(driver, 10) # Ждем конкретное условие
    driver.get(index_url)
    
    driver.find_element(By.CSS_SELECTOR, "#start button").click()
    
    start_time = time.time()
    # Ждем, пока элемент не станет видимым
    el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))
    elapsed = time.time() - start_time
    
    assert el.text == "Hello World!"
    print(f"\n[Explicit Wait] Элемент найден за {elapsed:.2f} сек.")