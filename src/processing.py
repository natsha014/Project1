def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает список словарей и значение для ключа,
    возвращает список словарей с указанным ключом"""
    return [i for i in list_dict if state == i.get("state")]


def sort_by_date(list_dict: list, reverse: bool = True) -> list:
    """Принимает список словарей и необязательный параметр сортировки
    (по умолчанию - убывание).
    Возвращает новый список, отсортированный по дате"""
    filtered_list = [d for d in list_dict if d.get("date") is not None]
    return sorted(filtered_list, key=lambda i: i.get("date"), reverse=reverse)
