import json
import logging
from typing import List, Dict, Any

def simple_search(transactions: List[Dict[str, Any]], query: str) -> str:
    """
    Ищет query в полях 'Категория' и 'Описание' (регистронезависимо).
    transactions – список словарей (можно получить из DataFrame: df.to_dict('records')).
    Возвращает JSON со списком подходящих транзакций.
    """
    query_lower = query.lower()
    results = []
    for t in transactions:
        cat = t.get('Категория', '').lower()
        desc = t.get('Описание', '').lower()
        if query_lower in cat or query_lower in desc:
            results.append(t)
    return json.dumps(results, ensure_ascii=False, indent=2, default=str)