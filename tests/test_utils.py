import pytest
from datetime import datetime
from src.utils import get_greeting, get_data_time, get_card_with_spend
import pandas as pd

def test_get_greeting():
    assert get_greeting(datetime(2021, 12, 20, 8, 0, 0)) == "Доброе утро"
    assert get_greeting(datetime(2021, 12, 20, 14, 0, 0)) == "Добрый день"
    assert get_greeting(datetime(2021, 12, 20, 20, 0, 0)) == "Добрый вечер"
    assert get_greeting(datetime(2021, 12, 20, 2, 0, 0)) == "Доброй ночи"

def test_get_data_time():
    result = get_data_time("2021-12-20 15:30:00")
    assert len(result) == 2
    assert result[0].startswith("01.12.2021")
    assert result[1].startswith("20.12.2021")

def test_get_card_with_spend_empty():
    # Передаём пустой DataFrame
    empty_df = pd.DataFrame(columns=['Номер карты', 'Сумма операции'])
    assert get_card_with_spend(empty_df) == []