# tests/ui/test_login.py
import time

import pytest

from pages.login_page import LoginPage
from conftest import driver


@pytest.mark.smoke
def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    time.sleep(1)
    assert "You logged into a secure area!" in page.get_flash_message()