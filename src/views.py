import json
from typing import Dict, Any
from utils import get_data_time, get_path_and_periods, get_card_with_spend, get_greeting
from datetime import datetime

def main_info(date_time: str) -> str:
    dt = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    greeting = get_greeting(dt)

    time_period = get_data_time(date_time)
    sorted_df = get_path_and_periods("../data/operations.xlsx", time_period)
    cards = get_card_with_spend(sorted_df)
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