from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():
    """
    Створює і повертає екземпляр Chrome WebDriver.
    Headless-режим вмикається автоматично для CI (GitHub Actions).
    """
    options = Options()
    options.add_argument("--headless=new")        # без GUI (потрібно для CI)
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")           # обов'язково для Linux CI
    options.add_argument("--disable-dev-shm-usage")  # уникає краш на CI

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver