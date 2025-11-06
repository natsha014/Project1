import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("my_apikey")
url = "https://api.apilayer.com/exchangerates_data/convert"


def amount_transactions(transactions: list[dict] | dict) -> float:
    """функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    for trans in transactions:
        currency = trans.get("operationAmount", {}).get("currency", {}).get("code")
        amount_cur = float(trans.get("operationAmount", {}).get("amount"))
        if currency == "RUB":
            amount = amount_cur
            print(amount)
        else:
            payload = {"amount": amount_cur, "from": currency, "to": "RUB"}
            headers = {"apikey": api_key}

            response = requests.get(url, headers=headers, params=payload)

            status_code = response.status_code
            print(status_code)
            if status_code == 200:
                result = response.json()
                amount = round(float(result.get("result")), 2)
                print(amount)
    return amount
