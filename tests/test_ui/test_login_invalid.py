import time

import pytest

from pages.login_page import LoginPage
from conftest import driver

''' Без Page Object '''
# def test_login_invalid_credentials(driver):
#     driver.get("https://the-internet.herokuapp.com/login")
#
#     # Вводим неверный логин и пароль
#     driver.find_element("id", "username").send_keys("wronguser")
#     driver.find_element("id", "password").send_keys("wrongpass")
#     driver.find_element("css selector", "button[type='submit']").click()
#
#     # Проверяем наличие сообщения об ошибке
#     flash_message = driver.find_element("id", "flash").text
#     assert "Your username is invalid" in flash_message

'''Сложный Page Object'''
# def test_fake_login(driver):
#     login_page = LoginPage(driver)
#     login_page.open()
#     login_page.enter_username("wronguser")
#     login_page.enter_password("wrongpass")
#     login_page.click_login_button()
#
#     message_alert = login_page.get_flash_message()
#     assert "Your username is invalid" in message_alert

# test_login_invalid.py

@pytest.mark.parametrize("username, password", [
    ("wrong", "SuperSecretPassword!"),      # неправильный логин
    ("tomsmith", "wrongpassword"),          # неправильный пароль
    ("wronguser", "wrongpass")              # всё неправильно
])
@pytest.mark.regression
def test_login_with_invalid_credentials(driver, username, password):
    page = LoginPage(driver)
    page.open()
    page.login(username, password)
    time.sleep(1)
    assert "Your username is invalid!" or "Your password is invalid!" in page.get_flash_message()
