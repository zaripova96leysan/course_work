import json
from src.views import main_info

def test_main_info_returns_valid_json():
    result = main_info("2021-12-20 15:30:00")
    data = json.loads(result)   # проверяем, что это JSON
    assert "greeting" in data
    assert "cards" in data
    assert "top_transactions" in data
    assert "currency_rates" in data
    assert "stock_prices" in data
    assert isinstance(data["cards"], list)