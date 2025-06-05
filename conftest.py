# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Безголовый режим (можно убрать для визуального теста)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()  # Можно указать путь к chromedriver, если он не в PATH: Service("путь/к/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)

    yield driver  # Передаём браузер в тест
    driver.quit()  # После выполнения теста — закрываем браузер
