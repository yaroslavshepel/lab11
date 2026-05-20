from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    """Page Object для сторінки /checkboxes."""

    URL = "https://the-internet.herokuapp.com/checkboxes"

    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    def open(self):
        super().open(self.URL)

    def select_all(self):
        """Вмикає всі чекбокси, які ще не вибрані."""
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        for cb in checkboxes:
            if not cb.is_selected():
                cb.click()

    def deselect_all(self):
        """Вимикає всі чекбокси."""
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        for cb in checkboxes:
            if cb.is_selected():
                cb.click()

    def all_selected(self):
        """Повертає True якщо всі чекбокси вибрані."""
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        return all(cb.is_selected() for cb in checkboxes)

    def none_selected(self):
        """Повертає True якщо жоден чекбокс не вибраний."""
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        return not any(cb.is_selected() for cb in checkboxes)