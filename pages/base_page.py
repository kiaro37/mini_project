from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://the-internet.herokuapp.com"

    def open(self, url=""):
        self.driver.get(f"{self.base_url}/{url}")

    def find_element(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Элемент с локатором {locator} не найден за {timeout} секунд")

    def click(self, locator, timeout=5):
        element = self.find_element(locator, timeout)
        element.click()

    def input_text(self, locator, text, timeout=5):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=5):
        element = self.find_element(locator, timeout)
        return element.text
