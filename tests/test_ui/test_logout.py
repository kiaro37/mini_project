# tests/test_logout.py
import time

from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from conftest import driver

def test_logout(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    time.sleep(1)
    # Убедимся, что вошли
    #assert page.is_logout_button_visible()

    # Выходим
    secure_page = SecurePage(driver)
    secure_page.logout()
    time.sleep(1)
    # Проверяем flash-сообщение
    assert "You logged out of the secure area!" in page.get_flash_message()
