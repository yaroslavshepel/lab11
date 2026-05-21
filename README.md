# Лабораторна робота 11 — Автоматизація UI-тестування з Selenium WebDriver

Автоматизовані UI-тести для сайту [the-internet.herokuapp.com](https://the-internet.herokuapp.com) з використанням Selenium WebDriver, Page Object Model, pytest та Allure Reports.

---

## Структура проєкту

```
selenium-lab/
│
├── pages/                        # Page Object класи
│   ├── base_page.py              # Базовий клас (find, click, type, get_text)
│   ├── login_page.py             # Сторінка /login
│   ├── checkboxes_page.py        # Сторінка /checkboxes
│   ├── alerts_page.py            # Сторінка /javascript_alerts
│   ├── frames_page.py            # Сторінка /nested_frames
│   └── windows_page.py           # Сторінка /windows
│
├── tests/                        # Тести
│   ├── conftest.py               # Pytest fixture драйвера + автоскрін при падінні
│   ├── test_login.py             # Тести логіну (в т.ч. параметризовані)
│   ├── test_checkboxes.py        # Тести чекбоксів
│   ├── test_alerts.py            # Тести Alert / Confirm / Prompt
│   ├── test_frames.py            # Тести вкладених фреймів
│   └── test_windows.py           # Тести роботи з вкладками
│
├── utils/
│   └── driver_setup.py           # Функція get_driver() для headless Chrome
│
├── .github/workflows/
│   └── tests.yml                 # GitHub Actions CI/CD пайплайн
│
├── requirements.txt              # Залежності Python
├── pytest.ini                    # Конфігурація pytest (allure-results)
└── README.md                     # Ця інструкція
```

---

## Вимоги

- Python 3.10+
- Google Chrome (встановлений на машині)
- ChromeDriver **не потрібно завантажувати вручну** — Selenium 4.x завантажує його автоматично через `selenium-manager`

---

## Локальний запуск

### 1. Клонувати репозиторій

```bash
git clone https://github.com/<ваш-username>/selenium-lab.git
cd selenium-lab
```

### 2. Встановити залежності

```bash
pip install -r requirements.txt
```

### 3. Запустити всі тести

```bash
pytest
```

### 4. Запустити окремий файл тестів

```bash
pytest tests/test_login.py
pytest tests/test_alerts.py
pytest tests/test_frames.py
pytest tests/test_windows.py
```

### 5. Запустити конкретний тест за назвою

```bash
pytest -k "test_invalid_login"
pytest -k "test_js_alert_accept"
```

### 6. Запустити тести паралельно (pytest-xdist)

```bash
pytest -n 4
```

---

## Allure звіт

### Локально

```bash
# Запуск тестів із збором результатів (pytest.ini вже налаштований)
pytest

# Відкрити звіт у браузері
allure serve allure-results
```

> Якщо `allure` не встановлений — завантажити з [allure.qatools.io](https://allurereport.org/docs/install/) або через `brew install allure` (macOS) / `scoop install allure` (Windows)

### У GitHub Actions

Після кожного push результати автоматично зберігаються як артефакт у розділі **Actions → ваш workflow → Artifacts → allure-results**.

---

## Змінні середовища

Жодних змінних середовища не потрібно — тестовий сайт публічний, креденшіали захардкоджені для тренування:

| Поле     | Значення              |
|----------|-----------------------|
| username | `tomsmith`            |
| password | `SuperSecretPassword!`|

---

## Що тестується

| Файл тестів          | Сторінка                  | Що перевіряється                                              |
|----------------------|---------------------------|---------------------------------------------------------------|
| `test_login.py`      | `/login`                  | Невірний логін, успішний логін, параметризовані комбінації    |
| `test_checkboxes.py` | `/checkboxes`             | Вибір усіх чекбоксів, зняття вибору                          |
| `test_alerts.py`     | `/javascript_alerts`      | Alert (OK), Confirm (OK/Cancel), Prompt (введення тексту)    |
| `test_frames.py`     | `/nested_frames`          | Текст у кожному фреймі, помилковий контекст, параметризація  |
| `test_windows.py`    | `/windows`                | Відкриття/закриття вкладок, перемикання, 4 сценарії          |

---

## Технічні рішення

**Page Object Model** — кожна сторінка описана окремим класом у `pages/`. Тест містить лише бізнес-логіку, без прямих звернень до Selenium API.

**Explicit waits** — використовується виключно `WebDriverWait`. `time.sleep()` у тестах відсутній.

**Автоскрін при падінні** — `conftest.py` перехоплює кожен тест через `pytest_runtest_makereport` і при падінні автоматично робить скріншот та додає його в Allure-звіт.

**Headless-режим** — Chrome запускається без GUI через `--headless=new`, що забезпечує коректну роботу в CI/CD.
