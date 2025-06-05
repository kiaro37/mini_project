from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.radius")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button.secondary.radius")
    FLASH_MESSAGE = (By.ID, "flash")

    def open(self):
        super().open("login")

    def login(self, username, password):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_flash_message(self):
        return self.get_text(self.FLASH_MESSAGE)

    def logout(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()

    def is_logout_button_visible(self):
        return self.driver.find_element(*self.LOGOUT_BUTTON).is_displayed()