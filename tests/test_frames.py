import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.frames_page import NestedFramesPage


@allure.title("Кількість фреймів верхнього рівня")
def test_top_level_frames_count(driver):
    """
    Assert: на сторінці рівно 2 фрейми верхнього рівня
            (frame-top і frame-bottom)
    """
    page = NestedFramesPage(driver)
    page.open()

    count = page.count_top_level_frames()
    assert count == 2, f"Очікувалось 2 фрейми, знайдено: {count}"


@allure.title("Кількість вкладених фреймів у frame-top")
def test_nested_frames_count_in_top(driver):
    """
    Assert: у frame-top рівно 3 вкладені фрейми
            (left, middle, right)
    """
    page = NestedFramesPage(driver)
    page.open()

    count = page.count_nested_frames_in_top()
    assert count == 3, f"Очікувалось 3 вкладені фрейми, знайдено: {count}"


@allure.title("Текст у frame-left = 'LEFT'")
def test_frame_left_text(driver):
    page = NestedFramesPage(driver)
    page.open()

    page.switch_to_left()
    text = page.get_body_text()

    assert "LEFT" in text, f"Очікувалось 'LEFT', отримано: '{text}'"


@allure.title("Текст у frame-middle = 'MIDDLE'")
def test_frame_middle_text(driver):
    page = NestedFramesPage(driver)
    page.open()

    page.switch_to_middle()
    text = page.get_body_text()

    assert "MIDDLE" in text, f"Очікувалось 'MIDDLE', отримано: '{text}'"


@allure.title("Текст у frame-right = 'RIGHT'")
def test_frame_right_text(driver):
    page = NestedFramesPage(driver)
    page.open()

    page.switch_to_right()
    text = page.get_body_text()

    assert "RIGHT" in text, f"Очікувалось 'RIGHT', отримано: '{text}'"


@allure.title("Текст у frame-bottom = 'BOTTOM'")
def test_frame_bottom_text(driver):
    page = NestedFramesPage(driver)
    page.open()

    page.switch_to_bottom()
    text = page.get_body_text()

    assert "BOTTOM" in text, f"Очікувалось 'BOTTOM', отримано: '{text}'"


@allure.title("Демонстрація помилки неправильного контексту фрейму")
def test_wrong_frame_context_raises_error(driver):
    """
    Перевіряє, що елемент з frame-left НЕ доступний з контексту frame-middle.
    Це демонстрація того, навіщо потрібно правильно перемикати фрейми.
    """
    page = NestedFramesPage(driver)
    page.open()

    # Переходимо у frame-middle
    page.switch_to_middle()

    # Намагаємось знайти елемент з frame-left — це МАЄ кинути виняток
    with pytest.raises(NoSuchElementException):
        driver.find_element(By.XPATH, "//body[text()='LEFT']")


@allure.title("Параметризована перевірка всіх вкладених фреймів")
@pytest.mark.parametrize("frame_name, expected_text", [
    ("frame-left",   "LEFT"),
    ("frame-middle", "MIDDLE"),
    ("frame-right",  "RIGHT"),
])
def test_nested_frames_texts(driver, frame_name, expected_text):
    """
    Перевіряє текст у кожному вкладеному фреймі через параметризацію.
    """
    page = NestedFramesPage(driver)
    page.open()

    # Перемикаємось у frame-top, потім у потрібний вкладений фрейм
    driver.switch_to.default_content()
    driver.switch_to.frame("frame-top")
    driver.switch_to.frame(frame_name)

    actual_text = driver.find_element(By.TAG_NAME, "body").text.strip()
    assert expected_text in actual_text, \
        f"{frame_name}: очікувалось '{expected_text}', отримано '{actual_text}'"