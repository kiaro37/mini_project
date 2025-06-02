# tests/ui/test_login.py
import time

import pytest

from pages.login_page import LoginPage
from conftest import driver

# def test_valid_login(driver):
#     login_page = LoginPage(driver)
#     login_page.open()
#     login_page.enter_username("tomsmith")
#     login_page.enter_password("SuperSecretPassword!")
#     login_page.click_login_button()
#
#     time.sleep(1)  # Подождем появления результата (лучше позже заменить на явное ожидание)
#     message = login_page.get_flash_message()
#     assert "You logged into a secure area!" in message
@pytest.mark.smoke
def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    time.sleep(1)
    assert "You logged into a secure area!" in page.get_flash_message()