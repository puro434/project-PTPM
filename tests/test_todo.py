from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_todo(driver, index_url):
    wait = WebDriverWait(driver, 10)
    driver.get(index_url)
    
    # Вводим задачу
    driver.find_element(By.ID, "taskInput").send_keys("Купить хлеб")
    driver.find_element(By.ID, "addBtn").click()
    
    # Ждем появления элемента в списке
    item = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#taskList li")))
    assert item.text == "Купить хлеб"
    
    # Сохраняем скриншот (для отчета)
    driver.save_screenshot("screenshots/todo_success.png")