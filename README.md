# AQA Demo Project

## 📌 Описание

Этот проект демонстрирует навыки автоматизированного тестирования:
- API тестирование (`requests`)
- UI тестирование (`Selenium + Page Object`)
- Запуск тестов с `pytest`
- Генерация HTML-отчётов (`pytest-html`)

---

## 📁 Структура проекта

- project/
- │
- ├── tests/ # Все тесты (API и UI)
- - │ ├── test_api.py
- - │ └── test_login.py
- │
- ├── pages/ # Page Object модели для UI
- - │ └── login_page.py
- │
- ├── conftest.py # фикстуры для тестов (driver и т.д.)
- ├── requirements.txt # зависимости проекта
- ├── pytest.ini # конфигурация pytest
- ├── reports/ # HTML-отчеты
- - │ └── report.html
- └── README.md

## Запуск всех тестов
- pytest

## Запуск с HTML-отчетом
- pytest --html=reports/report.html

## 🔧 Используемые технологии
- Python 3.10+
- Pytest
- Requests
- Selenium
- Pytest-html

## 🧪 Покрытие
✅ API тесты:
- Получение данных одного пользователя
- Негативный сценарий (не найден)

✅ UI тесты:
- Успешный логин
- Ошибки при неверных данных
- Выход из системы

