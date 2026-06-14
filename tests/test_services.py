import json
from src.services import simple_search

def test_simple_search():
    transactions = [
        {"Категория": "Супермаркеты", "Описание": "Пятёрочка"},
        {"Категория": "Такси", "Описание": "Яндекс Go"},
        {"Категория": "Переводы", "Описание": "Валерий А."}
    ]
    result = simple_search(transactions, "вал")
    data = json.loads(result)
    assert len(data) == 1
    assert data[0]["Категория"] == "Переводы"
    assert "Валерий" in data[0]["Описание"]

def test_search_case_insensitive():
    transactions = [{"Категория": "Аптеки", "Описание": "Apteka"}]
    result = simple_search(transactions, "apteka")
    data = json.loads(result)
    assert len(data) == 1