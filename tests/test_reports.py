import pytest
import pandas as pd
from src.reports import spending_by_category
import os
import json

@pytest.fixture
def sample_df():

    return pd.DataFrame({
        'Дата операции': pd.to_datetime(['2021-10-15', '2021-11-20', '2021-12-10']),
        'Категория': ['Супермаркеты', 'Супермаркеты', 'Такси'],
        'Сумма платежа': [-1000, -2000, -500],
        'Описание': ['test', 'test', 'test']
    })

def test_spending_by_category(sample_df):
    result = spending_by_category(sample_df, "Супермаркеты", "2021-12-20")
    assert isinstance(result, pd.DataFrame)
    assert result['amount'].sum() == 3000
    assert any(f.startswith("report_spending_by_category_") for f in os.listdir("."))
    for f in os.listdir("."):
        if f.startswith("report_spending_by_category_"):
            os.remove(f)