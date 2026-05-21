import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
from pathlib import Path
import time
from selenium.common.exceptions import SessionNotCreatedException, WebDriverException

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def _create_driver(options, attempts=2, delay_seconds=1):
    # Retry to avoid intermittent Chrome startup issues.
    last_error = None
    for _ in range(attempts):
        try:
            driver = webdriver.Chrome(options=options)
            driver.maximize_window()
            return driver
        except (SessionNotCreatedException, WebDriverException) as exc:
            last_error = exc
            time.sleep(delay_seconds)
    raise last_error


@pytest.fixture
def driver():
    """
    Pytest fixture: створює браузер перед кожним тестом
    і закриває його після, навіть якщо тест впав.
    """
    options = Options()
    options.add_argument("--headless=new")          # без GUI (для CI)
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = _create_driver(options)

    yield driver  # <-- тест виконується тут

    driver.quit()  # завжди закриває браузер після тесту


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Перехоплює результат кожного тесту.
    Якщо тест впав — автоматично робить скріншот і додає в Allure-звіт.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )