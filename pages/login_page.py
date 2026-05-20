from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object для сторінки /login.
    Тестові дані: username=tomsmith, password=SuperSecretPassword!
    """

    URL = "https://the-internet.herokuapp.com/login"

    # Локатори — кортежі (By.*, "значення")
    USERNAME  = (By.ID, "username")
    PASSWORD  = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH     = (By.ID, "flash")

    def open(self):
        """Відкриває сторінку логіну."""
        super().open(self.URL)

    def login(self, username, password):
        """Вводить дані і натискає кнопку Login."""
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_flash_text(self):
        """Повертає текст flash-повідомлення після спроби входу."""
        return self.get_text(self.FLASH)