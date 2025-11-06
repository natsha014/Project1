import re
from collections import Counter


def process_bank_search(transactions: list[dict], search_str: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""
    result = []
    for transaction in transactions:
        if "description" in transaction and isinstance(transaction["description"], str):
            if re.search(search_str, transaction["description"], flags=re.IGNORECASE):
                result.append(transaction)
    return result


def process_bank_operations(transactions: list[dict], categories: list) -> dict:
    """функция принимает список словарей с данными о банковских операциях и список категорий операций и
    возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""
    if not transactions or not isinstance(transactions, list):
        return {}

    category_list = []
    try:
        for transaction in transactions:
            for category in categories:
                if transaction.get("description") == category:
                    category_list.append(category)
        counted = Counter(category_list)
        return dict(counted)
    except Exception: #pragma: no cover
        return {}
