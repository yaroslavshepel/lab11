from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class AlertsPage(BasePage):
    """
    Page Object для сторінки /javascript_alerts.
    Містить методи для роботи з Alert, Confirm та Prompt.
    """

    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    # Кнопки виклику алертів — використовуємо text() у XPath
    # (тут XPath виправданий: кнопки не мають id чи унікального CSS)
    ALERT_BTN   = (By.XPATH, "//button[text()='Click for JS Alert']")
    CONFIRM_BTN = (By.XPATH, "//button[text()='Click for JS Confirm']")
    PROMPT_BTN  = (By.XPATH, "//button[text()='Click for JS Prompt']")

    RESULT = (By.ID, "result")  # текст результату після закриття алерту

    def open(self):
        super().open(self.URL)

    # --- Кнопки ---

    def click_alert(self):
        """Натискає кнопку 'Click for JS Alert'."""
        self.click(self.ALERT_BTN)

    def click_confirm(self):
        """Натискає кнопку 'Click for JS Confirm'."""
        self.click(self.CONFIRM_BTN)

    def click_prompt(self):
        """Натискає кнопку 'Click for JS Prompt'."""
        self.click(self.PROMPT_BTN)

    # --- Дії з алертом ---

    def accept(self):
        """Чекає появи алерту і натискає OK."""
        self.wait.until(EC.alert_is_present()).accept()

    def dismiss(self):
        """Чекає появи алерту і натискає Cancel."""
        self.wait.until(EC.alert_is_present()).dismiss()

    def send_text_to_alert(self, text):
        """Вводить текст у Prompt і підтверджує (OK)."""
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys(text)
        alert.accept()

    # --- Результат ---

    def get_result_text(self):
        """Повертає текст з блоку result після дії з алертом."""
        return self.get_text(self.RESULT)