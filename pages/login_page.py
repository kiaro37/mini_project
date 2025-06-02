# pages/login_page.py
# from selenium.webdriver.common.by import By
#
# class LoginPage:
#     URL = "https://the-internet.herokuapp.com/login"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def open(self):
#         self.driver.get(self.URL)
#
#     def enter_username(self, username):
#         self.driver.find_element(By.ID, "username").send_keys(username)
#
#     def enter_password(self, password):
#         self.driver.find_element(By.ID, "password").send_keys(password)
#
#     def click_login_button(self):
#         self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#
#     def get_flash_message(self):
#         return self.driver.find_element(By.ID, "flash").text

# pages/login_page.py

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/login"
        self.username_input = ("id", "username")
        self.password_input = ("id", "password")
        self.login_button = ("css selector", "button[type='submit']")
        self.logout_button = ("css selector", "a.button.secondary.radius")
        self.flash_message = ("id", "flash")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def logout(self):
        self.driver.find_element(*self.logout_button).click()

    def get_flash_message(self):
        return self.driver.find_element(*self.flash_message).text

    def is_logout_button_visible(self):
        return self.driver.find_element(*self.logout_button).is_displayed()