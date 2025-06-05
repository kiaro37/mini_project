# pages/secure_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SecurePage(BasePage):
    LOGOUT_BUTTON = (By.XPATH, "//a[@class='button secondary radius']")
    FLASH_MESSAGE = (By.ID, "flash")

    def logout(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()

    def get_flash_message(self):
        return self.driver.find_element(*self.FLASH_MESSAGE).text
