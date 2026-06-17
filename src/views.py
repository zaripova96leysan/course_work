import json
from typing import Dict, Any
from utils import get_data_time, get_path_and_periods, get_card_with_spend, get_greeting
from datetime import datetime
import pandas as pd

def main_info(date_time: str) -> str:
    dt = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    greeting = get_greeting(dt)

    time_period = get_data_time(date_time)
    sorted_df = get_path_and_periods("../data/operations.xlsx", time_period)
    cards = get_card_with_spend(sorted_df)


    if not sorted_df.empty:
        sorted_df_copy = sorted_df.copy()
        sorted_df_copy['abs_amount'] = sorted_df_copy['Сумма платежа'].abs()
        top5 = sorted_df_copy.nlargest(5, 'abs_amount')
        top_transactions = []
        for _, row in top5.iterrows():

            if isinstance(row['Дата операции'], pd.Timestamp):
                date_str = row['Дата операции'].strftime('%d.%m.%Y')
            else:
                date_str = str(row['Дата операции'])
            top_transactions.append({
                "date": date_str,
                "amount": round(row['Сумма платежа'], 2),
                "category": row['Категория'] if pd.notna(row['Категория']) else "",
                "description": row['Описание'] if pd.notna(row['Описание']) else ""
            })
    else:
        top_transactions = []



    currency_rates = []
    stock_prices = []

    data = {
        "greeting": greeting,
        "cards": cards,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices
    }
    return json.dumps(data, ensure_ascii=False, indent=4)