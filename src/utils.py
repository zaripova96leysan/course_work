from datetime import datetime
from pandas import DataFrame
import pandas as pd
import json

def get_time_for_greeting():
    """
    Фнкция, которая возвращает «Доброе утро»/ «Добрый день» / «Добрый вечер»
    / «Доброй ночи» в зависимости от текущего времени.
    """
    user_datetime_hour = datetime.now().hour
    if 5 <= user_datetime_hour < 12:
        return "Доброе утро"
    elif 12 <= user_datetime_hour < 18:
        return "Добрый день"
    elif 18 <= user_datetime_hour < 22:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def get_data_time(date_time: str, date_format: str = "%Y-%m-%d %H:%M:%S") -> list[str]:
    dt = datetime.strptime(date_time, date_format)
    start_of_month = dt.replace(day=1)
    return [
        start_of_month.strftime("%d.%m.%Y %H:%M:%S"),
        dt.strftime("%d.%m.%Y %H:%M:%S")
    ]

def get_path_and_periods(path_to_file: str, period_date: list) -> pd.DataFrame:
    """ Загружает транзакции из Excel"""
    df = pd.read_excel(path_to_file)
    df['Дата операции'] = pd.to_datetime(df['Дата операции'], dayfirst=True)
    start_date = datetime.strptime(period_date[0], "%d.%m.%Y %H:%M:%S")
    end_date = datetime.strptime(period_date[1], "%d.%m.%Y %H:%M:%S")
    filtered_df = df[(df["Дата операции"] >= start_date) & (df["Дата операции"] <= end_date)]
    return filtered_df


def get_card_with_spend(sorted_df: DataFrame) -> list[dict]:
    """ Функция, которая принимает DataFrame и возвращает список карт с расходами """
    expenses = sorted_df[sorted_df["Сумма операции"] < 0].copy()
    if expenses.empty:
        return []

    card_sum = {}
    for index, row in expenses.iterrows():
        card = row["Номер карты"]
        amount = row["Сумма операции"]
        # Суммируем (amount отрицательное, поэтому вычитаем или складываем)
        card_sum[card] = card_sum.get(card, 0) + abs(amount)

    # 3. Формируем результат
    card_spent_transactions = []
    for card, total_spent in card_sum.items():
        last_digits = str(card).replace("*", "")[-4:]
        cashback = total_spent / 100  # 1 рубль на каждые 100 рублей
        card_spent_transactions.append({
            "last_digits": last_digits,
            "total_spent": round(total_spent, 2),
            "cashback": round(cashback, 2)
        })
    return card_spent_transactions


def load_user_settings(settings_path: str = "user_settings.json") -> Dict[str, Any]:
    """
    Загружает настройки пользователя (валюты и акции) из JSON-файла.
    """
    try:
        with open(settings_path, 'r', encoding='utf-8') as f:
            settings = json.load(f)
        return settings
    except FileNotFoundError:
        return {"user_currencies": ["USD", "EUR"], "user_stocks": []}
    except json.JSONDecodeError:
        return {"user_currencies": ["USD", "EUR"], "user_stocks": []}