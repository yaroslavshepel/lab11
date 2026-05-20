from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    """
    Базовий клас для всіх Page Object.
    Містить спільні методи: пошук, клік, введення тексту, очікування.
    Всі дочірні сторінки наслідують ці методи автоматично.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # явне очікування до 10 секунд

    def open(self, url):
        """Відкриває URL у браузері."""
        self.driver.get(url)

    def find(self, locator):
        """
        Чекає поки елемент з'явиться у DOM і повертає його.
        locator — кортеж, наприклад (By.ID, "username")
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Чекає поки елемент стане клікабельним і натискає його."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        """Знаходить поле, очищає його і вводить текст."""
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        """Повертає текстовий вміст елемента."""
        return self.find(locator).text

    def is_visible(self, locator):
        """Повертає True якщо елемент видимий на сторінці."""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except Exception:
            return False

    def get_text_from_frame(self, frame_name):
        """
        Перемикається у вказаний фрейм, зчитує текст body і повертається назад.
        Використовується у тестах фреймів.
        """
        self.driver.switch_to.frame(frame_name)
        text = self.driver.find_element(By.TAG_NAME, "body").text.strip()
        self.driver.switch_to.default_content()
        return text