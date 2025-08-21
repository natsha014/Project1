def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Принимает список словарей и значение для ключа,
    возвращает список словарей с указанным ключом"""
    return [i for i in list_dict if state == i["state"]]


def sort_by_date(list_dict: list, reverse: bool = True) -> list:
    """Принимает список словарей и необязательный параметр сортировки
    (по умолчанию - убывание).
    Возврвщает новый список, отсортированный по дате"""
    return sorted(list_dict, key=lambda i: i["date"], reverse=True)
