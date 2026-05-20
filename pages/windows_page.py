from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class WindowsPage(BasePage):
    """
    Page Object для сторінки /windows.
    Демонструє роботу з кількома вкладками браузера.
    """

    URL = "https://the-internet.herokuapp.com/windows"

    CLICK_HERE  = (By.LINK_TEXT, "Click Here")
    NEW_WIN_H3  = (By.TAG_NAME, "h3")

    def open(self):
        super().open(self.URL)

    def get_current_window(self):
        """Повертає handle (ідентифікатор) поточної вкладки."""
        return self.driver.current_window_handle

    def click_open_new_window(self):
        """Натискає посилання 'Click Here' для відкриття нової вкладки."""
        self.click(self.CLICK_HERE)

    def switch_to_new_window(self, original_window):
        """
        Чекає появи нової вкладки і перемикається у неї.
        Знаходить нову вкладку БЕЗ індексів (handles[1]) —
        фільтрує список за збереженим original_window.
        """
        self.wait.until(EC.number_of_windows_to_be(2))
        new_window = [
            w for w in self.driver.window_handles
            if w != original_window
        ][0]
        self.driver.switch_to.window(new_window)

    def switch_to_window(self, handle):
        """Перемикається у вкладку за збереженим handle."""
        self.driver.switch_to.window(handle)

    def close_current_window(self):
        """Закриває поточну вкладку (не весь браузер)."""
        self.driver.close()

    def get_new_window_header(self):
        """Повертає текст заголовку нової вкладки."""
        return self.get_text(self.NEW_WIN_H3)

    def wait_for_n_windows(self, n):
        """Чекає поки кількість відкритих вкладок стане рівною n."""
        self.wait.until(EC.number_of_windows_to_be(n))

    def get_all_window_handles(self):
        """Повертає список усіх відкритих вкладок."""
        return self.driver.window_handles

    def is_button_present(self):
        """Перевіряє, що кнопка 'Click Here' доступна на поточній сторінці."""
        return self.is_visible(self.CLICK_HERE)