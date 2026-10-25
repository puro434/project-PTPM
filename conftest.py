import os
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    
    # Если мы на GitHub Actions (Linux), включаем невидимый режим
    if os.getenv("GITHUB_ACTIONS"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")              # Обязательно для облака
        options.add_argument("--disable-dev-shm-usage")   # Обязательно для облака
        options.add_argument("--disable-gpu")             # Обязательно для облака
    
    d = webdriver.Chrome(options=options)
    yield d
    d.quit()