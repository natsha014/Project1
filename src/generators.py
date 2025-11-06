from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    """Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""
    for trans in transactions:
        trans_currency = trans.get("currency_code")

        if trans_currency == currency:
            yield trans


def transaction_descriptions(transactions: list) -> Iterator:
    """Функция принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
    for trans in transactions:
        yield trans.get("description")


def card_number_generator(start: int, stop: int) -> Iterator:
    """Генератор может сгенерировать номера карт в заданном диапазоне от
    0000 0000 0000 0001 до 9999 9999 9999 9999"""
    for number in range(start, stop + 1):
        num_str = f"{number:016d}"
        numb = f"{num_str[:4] + ' ' + num_str[4:8] + ' ' + num_str[8:12] + ' ' + num_str[12:]}"
        yield numb
