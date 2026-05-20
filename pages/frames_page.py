from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    """
    Page Object для сторінки /nested_frames.

    Ієрархія фреймів:
        default content
        ├── frame-top
        │   ├── frame-left
        │   ├── frame-middle
        │   └── frame-right
        └── frame-bottom

    Правило: перед кожним switch_to.frame()
    завжди повертатись у default_content().
    """

    URL = "https://the-internet.herokuapp.com/nested_frames"

    def open(self):
        super().open(self.URL)

    def switch_to_default(self):
        """Повертається у головний контекст сторінки."""
        self.driver.switch_to.default_content()

    def switch_to_top(self):
        """Переходить у верхній фрейм (frame-top)."""
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("frame-top")

    def switch_to_middle(self):
        """
        Переходить у середній вкладений фрейм (frame-middle).
        Спочатку потрібно перейти у frame-top.
        """
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("frame-top")
        self.driver.switch_to.frame("frame-middle")

    def switch_to_left(self):
        """Переходить у лівий вкладений фрейм (frame-left)."""
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("frame-top")
        self.driver.switch_to.frame("frame-left")

    def switch_to_right(self):
        """Переходить у правий вкладений фрейм (frame-right)."""
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("frame-top")
        self.driver.switch_to.frame("frame-right")

    def switch_to_bottom(self):
        """Переходить у нижній фрейм (frame-bottom)."""
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("frame-bottom")

    def get_body_text(self):
        """
        Зчитує текст з <body> поточного фрейму.
        Викликати після switch_to_*().
        """
        return self.driver.find_element(
            By.TAG_NAME, "body"
        ).text.strip()

    def count_top_level_frames(self):
        """Повертає кількість фреймів верхнього рівня (очікуємо 2)."""
        self.driver.switch_to.default_content()
        return len(self.driver.find_elements(
            By.CSS_SELECTOR, "frame, iframe"
        ))

    def count_nested_frames_in_top(self):
        """Повертає кількість вкладених фреймів у frame-top (очікуємо 3)."""
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("frame-top")
        count = len(self.driver.find_elements(By.CSS_SELECTOR, "frame"))
        self.driver.switch_to.default_content()
        return count