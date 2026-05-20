import pytest
import allure
from pages.login_page import LoginPage


@allure.title("Логін з некоректними даними")
def test_invalid_login(driver):
    """
    Arrange: відкрити сторінку логіну
    Act:     ввести невірний логін і пароль
    Assert:  flash-повідомлення містить 'invalid'
    """
    # Arrange
    page = LoginPage(driver)
    page.open()

    # Act
    page.login("wrong_user", "wrong_pass")

    # Assert
    flash = page.get_flash_text()
    assert "invalid" in flash, f"Очікувалось 'invalid' у: {flash}"


@allure.title("Успішний логін з коректними даними")
def test_valid_login(driver):
    """
    Arrange: відкрити сторінку логіну
    Act:     ввести правильні логін і пароль
    Assert:  flash-повідомлення містить 'You logged into a secure area!'
    """
    # Arrange
    page = LoginPage(driver)
    page.open()

    # Act
    page.login("tomsmith", "SuperSecretPassword!")

    # Assert
    flash = page.get_flash_text()
    assert "You logged into a secure area!" in flash, \
        f"Очікувалось повідомлення про успіх, отримано: {flash}"


@allure.title("Параметризований тест логіну")
@pytest.mark.parametrize("username, password, expected", [
    ("wrong",      "wrong",               "invalid"),
    ("tomsmith",   "SuperSecretPassword!", "You logged into a secure area!"),
    ("",           "",                    "invalid"),
    ("tomsmith",   "wrong_pass",          "invalid"),
])
def test_login_parametrized(driver, username, password, expected):
    """
    Перевіряє логін з різними комбінаціями даних.
    """
    page = LoginPage(driver)
    page.open()
    page.login(username, password)
    flash = page.get_flash_text()
    assert expected in flash, f"Очікувалось '{expected}' у: {flash}"