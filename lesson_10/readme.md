# Homework 10 — Автотесты с отчётом Allure

## Описание проекта
Проект содержит автотесты (pytest + Selenium) с использованием
Allure для формирования отчёта о результатах тестирования.

## Требования
- Python 3.10+
- Java (JDK 21) — нужна для запуска Allure
- Библиотеки из `requirements.txt`

## Установка
1. Создать и активировать виртуальное окружение:
```
python -m venv .venv 
.venv\Scripts\Activate.ps1
```
2. Установить зависимости:
```
pip install -r requirements.txt
```

## Запуск тестов
Тесты находятся в папке `lesson_10/tests`.

### Обычный запуск (без отчёта)
```
pytest lesson_10\tests
```

### Запуск с формированием результатов для Allure
```
pytest lesson_10\tests --alluredir=allure-results
```
Результаты прогонов сохраняются в папку `allure-results`.

## Просмотр отчёта

### Вариант 1: разовый просмотр (рекомендуется)
Allure сам сгенерирует отчёт и откроет его в браузере:
```
.\allure-2.46.2\bin\allure.bat serve allure-results
```

### Вариант 2: сохранение отчёта в папку
Сгенерировать отчёт в папку `allure-report`:
```
.\allure-2.46.2\bin\allure.bat generate allure-results -o allure-report --clean
```
Затем открыть файл `allure-report\index.html` в браузере.

## Структура отчёта
- **Overview** — общая статистика (сколько тестов пройдено/упало);
- **Suites** — тесты, сгруппированные по файлам и классам;
- внутри каждого теста — шаги (`allure.step`) со статусами.
