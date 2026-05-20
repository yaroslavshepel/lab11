import allure
from pages.checkboxes_page import CheckboxesPage


@allure.title("Вибір всіх чекбоксів")
def test_select_all_checkboxes(driver):
    """
    Arrange: відкрити сторінку з чекбоксами
    Act:     вибрати всі чекбокси
    Assert:  всі чекбокси вибрані
    """
    # Arrange
    page = CheckboxesPage(driver)
    page.open()

    # Act
    page.select_all()

    # Assert
    assert page.all_selected(), "Не всі чекбокси вибрані"


@allure.title("Зняття вибору з усіх чекбоксів")
def test_deselect_all_checkboxes(driver):
    """
    Arrange: відкрити сторінку, вибрати всі чекбокси
    Act:     зняти вибір з усіх
    Assert:  жоден чекбокс не вибраний
    """
    # Arrange
    page = CheckboxesPage(driver)
    page.open()
    page.select_all()

    # Act
    page.deselect_all()

    # Assert
    assert page.none_selected(), "Деякі чекбокси залишились вибраними"