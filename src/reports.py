import json
import pandas as pd
from datetime import datetime
from functools import wraps
from typing import Optional


def save_to_file(filename: Optional[str] = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                out_name = f"report_{func.__name__}_{timestamp}.json"
            else:
                out_name = filename
            with open(out_name, 'w', encoding='utf-8') as f:
                if isinstance(result, pd.DataFrame):
                    data = result.to_dict(orient='records')
                else:
                    data = result
                json.dump(data, f, ensure_ascii=False, indent=2, default=str)
            return result
        return wrapper
    return decorator


@save_to_file()
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """
    Возвращает траты по категории за последние 3 месяца от date.
    Если date не указана – от текущей даты.
    """
    df = transactions.copy()
    df['Дата операции'] = pd.to_datetime(df['Дата операции'], dayfirst=True)

    if date is None:
        end_date = datetime.now()
    else:
        try:
            end_date = pd.to_datetime(date, dayfirst=True)
        except:
            end_date = pd.to_datetime(date)

    start_date = end_date - pd.DateOffset(months=3)


    mask = (df['Категория'] == category) & (df['Дата операции'] >= start_date) & (df['Дата операции'] <= end_date)
    filtered = df.loc[mask]


    expenses = filtered[filtered['Сумма платежа'] < 0].copy()
    expenses['amount'] = expenses['Сумма платежа'].abs()

    result = expenses[['Дата операции', 'amount']].rename(columns={'Дата операции': 'date'})
    result.sort_values('date', inplace=True)
    return result