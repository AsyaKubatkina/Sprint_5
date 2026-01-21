# Sprint UI автотесты для сервиса «Доска»

UI-автотесты на Python + Selenium для учебного сервиса «Доска»:
https://qa-desk.stand.praktikum-services.ru/

## Стек
- Python
- Pytest
- Selenium WebDriver
- Google Chrome

## Структура проекта
- `tests/` — тесты и `conftest.py` (фикстуры)
- `locators.py` — локаторы элементов
- `data.py` — тестовые данные/генераторы
- `requirements.txt` — зависимости проекта
- `.gitignore` — файлы, которые не нужно коммитить

## Установка и запуск (macOS)

1. Создать и активировать виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate

2. Установить зависимости:
pip install -r requirements.txt

3. Запустить все тесты:
pytest -v

4. Запуск конкретного файла:
pytest -v tests/test_registration.py

Покрытие тестами
	•	Регистрация пользователя (валидная / невалидная / существующий пользователь)
	•	Login пользователя
	•	Logout пользователя
	•	Создание объявления неавторизованным пользователем
	•	Создание объявления авторизованным пользователем
