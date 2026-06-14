# Анализ транзакций

## Установка
1. Создать виртуальное окружение: `python -m venv .venv`
2. Активировать: `.venv\Scripts\activate` (Windows) или `source .venv/bin/activate` (Mac/Linux)
3. Установить зависимости: `pip install pandas openpyxl requests pytest`

## Запуск
`python main.py`

## Задачи
- Главная страница (`views.py`) – JSON с приветствием, расходами по картам, топ‑5 транзакций.
- Простой поиск (`services.py`) – поиск по категории и описанию.
- Отчёт по категории (`reports.py`) – траты за 3 месяца + декоратор для сохранения в JSON.

## Данные
Файл `data/operations.xlsx` с транзакциями.

## Тесты
`pytest tests/`