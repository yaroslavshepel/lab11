import allure
from pages.windows_page import WindowsPage


@allure.title("Сценарій 1: Відкрити нову вкладку і перевірити заголовок")
def test_open_new_window_and_check_header(driver):
    """
    Arrange: відкрити сторінку, зберегти original_window
    Act:     клікнути 'Click Here', перемкнутись у нову вкладку
    Assert:  заголовок нової вкладки = 'New Window'
    """
    # Arrange
    page = WindowsPage(driver)
    page.open()
    original_window = page.get_current_window()

    # Act
    page.click_open_new_window()
    page.switch_to_new_window(original_window)

    # Assert
    header = page.get_new_window_header()
    assert header == "New Window", \
        f"Очікувався заголовок 'New Window', отримано: '{header}'"


@allure.title("Сценарій 2: Закрити нову вкладку і повернутись на оригінальну")
def test_close_new_window_and_return(driver):
    """
    Arrange: відкрити нову вкладку
    Act:     закрити нову вкладку, повернутись на оригінальну
    Assert:  кнопка 'Click Here' знову доступна
    """
    # Arrange
    page = WindowsPage(driver)
    page.open()
    original_window = page.get_current_window()
    page.click_open_new_window()
    page.switch_to_new_window(original_window)

    # Act — закрити нову вкладку і повернутись
    page.close_current_window()
    page.switch_to_window(original_window)

    # Assert — кнопка доступна і можна відкрити ще одну вкладку
    assert page.is_button_present(), \
        "Кнопка 'Click Here' недоступна після повернення на оригінальну вкладку"


@allure.title("Сценарій 3: Чекаємо появи нової вкладки через WebDriverWait")
def test_wait_for_new_window(driver):
    """
    Демонструє правильне очікування появи нової вкладки
    через WebDriverWait замість time.sleep().
    """
    page = WindowsPage(driver)
    page.open()
    original_window = page.get_current_window()

    page.click_open_new_window()

    # switch_to_new_window всередині чекає через WebDriverWait
    page.switch_to_new_window(original_window)

    # Перевіряємо наявність тексту 'New Window' у джерелі сторінки
    header = page.get_new_window_header()
    assert header == "New Window", \
        f"Текст 'New Window' не знайдено на новій вкладці, отримано: '{header}'"


@allure.title("Сценарій 4: Відкрити 2 нові вкладки і перевірити кожну")
def test_open_two_windows_and_check_all(driver):
    """
    Arrange: відкрити сторінку, зберегти original_window
    Act:     двічі клікнути 'Click Here' — відкрити 2 нові вкладки
    Assert:  у кожній новій вкладці є текст 'New Window',
             на першій — є 'Opening a new window'
    """
    # Arrange
    page = WindowsPage(driver)
    page.open()
    original_window = page.get_current_window()

    # Act — відкрити 2 нові вкладки
    page.click_open_new_window()
    page.wait_for_n_windows(2)

    page.switch_to_window(original_window)  # повернутись для другого кліку
    page.click_open_new_window()
    page.wait_for_n_windows(3)

    # Assert — перевірити всі вкладки
    all_handles = page.get_all_window_handles()
    assert len(all_handles) == 3, \
        f"Очікувалось 3 вкладки, відкрито: {len(all_handles)}"

    new_windows = [w for w in all_handles if w != original_window]
    for handle in new_windows:
        page.switch_to_window(handle)
        header = page.get_new_window_header()
        assert header == "New Window", \
            f"Текст 'New Window' не знайдено у вкладці {handle}"

    # Перевірка оригінальної вкладки
    page.switch_to_window(original_window)
    assert "Opening a new window" in driver.page_source, \
        "Текст 'Opening a new window' не знайдено на оригінальній вкладці"