import allure
from pages.alerts_page import AlertsPage


@allure.title("JS Alert — прийняти (OK)")
def test_js_alert_accept(driver):
    """
    Arrange: відкрити сторінку алертів
    Act:     викликати Alert і натиснути OK
    Assert:  результат містить 'You successfully clicked an alert'
    """
    # Arrange
    page = AlertsPage(driver)
    page.open()

    # Act
    page.click_alert()
    page.accept()

    # Assert
    result = page.get_result_text()
    assert "You successfully clicked an alert" in result, \
        f"Неочікуваний результат: {result}"


@allure.title("JS Confirm — підтвердити (OK)")
def test_js_confirm_accept(driver):
    """
    Act:    викликати Confirm і натиснути OK
    Assert: результат містить 'Ok'
    """
    page = AlertsPage(driver)
    page.open()

    page.click_confirm()
    page.accept()

    result = page.get_result_text()
    assert "Ok" in result, f"Неочікуваний результат: {result}"


@allure.title("JS Confirm — скасувати (Cancel)")
def test_js_confirm_dismiss(driver):
    """
    Act:    викликати Confirm і натиснути Cancel
    Assert: результат містить 'Cancel'
    """
    page = AlertsPage(driver)
    page.open()

    page.click_confirm()
    page.dismiss()

    result = page.get_result_text()
    assert "Cancel" in result, f"Неочікуваний результат: {result}"


@allure.title("JS Prompt — ввести текст і підтвердити")
def test_js_prompt_send_text(driver):
    """
    Act:    викликати Prompt, ввести 'Hello' і натиснути OK
    Assert: результат містить 'Hello'
    """
    page = AlertsPage(driver)
    page.open()

    page.click_prompt()
    page.send_text_to_alert("Hello")

    result = page.get_result_text()
    assert "Hello" in result, f"Введений текст не відобразився: {result}"