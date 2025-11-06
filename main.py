import re

from src.generators import filter_by_currency
from src.masks import get_mask_account
from src.masks import get_mask_card
from src.process_bank import process_bank_search
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.read_data import read_csv
from src.read_data import read_excel
from src.utils import load_operations

files = {"1": "JSON", "2": "CSV", "3": "XLSX"}

json_f = load_operations("data/operations.json")
csv_f = read_csv("data/transactions.csv")
xlsx_f = read_excel("data/transactions_excel.xlsx")

file = {"JSON": json_f, "CSV": csv_f, "XLSX": xlsx_f}

statuses = ["EXECUTED", "CANCELED", "PENDING"]


def main() -> None:
    """Функция отвечает за основную логику проекта и связывает функциональности между собой"""
    user_file = input(
        """
    Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла

    Пользователь:  """
    )

    if user_file in files:
        selected_file = files[user_file]
        print(f"Программа: Для обработки выбран {selected_file}-файл")
        f = list(file[selected_file])
        user_state = input(
            """Программа: Введите статус, по которому необходимо выполнить фильтрацию.
           Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
Пользователь:  """
        ).upper()

        if user_state in statuses:
            print(f"Программа: Операции отфильтрованы по статусу {user_state}")
            st = filter_by_state(f, user_state)

            user_date = input(
                """Программа: Отсортировать операции по дате? Да/Нет
Пользователь:  """
            ).lower()
            if user_date == "да":
                user_date_1 = input(
                    """Программа: Отсортировать по возрастанию или по убыванию?
Пользователь:  """
                ).lower()
                if user_date_1 == "по возрастанию":
                    dt = sort_by_date(st, False)
                elif user_date_1 == "по убыванию":
                    dt = sort_by_date(st)
            else:
                dt = st

            user_cur = input(
                """Программа: Выводить только рублевые транзакции? Да / Нет
Пользователь:  """
            ).lower()
            if user_cur == "да":
                cur = list(filter_by_currency(dt, "RUB"))
            elif user_cur == "нет":
                cur = dt

            user_s = input(
                """Программа: Отфильтровать список транзакций
           по определенному слову в описании? Да / Нет
Пользователь:  """
            )
            if user_s == "да":
                user_s_1 = input(
                    """Программа: Введите слово для фильтрации
Пользователь:  """
                ).lower()
                if user_s_1:
                    sear = process_bank_search(cur, user_s_1)
            elif user_s == "нет":
                sear = cur

            account_pattern = r"(\d{20})"
            card_pattern = r"(\d{16})"

            for i in sear:
                for key in ["to", "from"]:
                    if key in i and i[key]:
                        text = i[key]
                        match_1 = re.search(account_pattern, text)
                        match_2 = re.search(card_pattern, text)
                        if match_1:
                            acc_num = match_1.group(1)
                            masked_acc = get_mask_account(acc_num)
                            i[key] = text.replace(acc_num, masked_acc)
                        elif match_2:
                            car_num = match_2.group(1)
                            masked_car = get_mask_card(car_num)
                            i[key] = text.replace(car_num, masked_car)

            counted = len(sear)

            if len(sear) > 0:
                print("Программа: Распечатываю итоговый список транзакций...")
                print(
                    f"""Программа:
                    Всего банковских операций в выборке: {counted}"""
                )
                for s in sear:
                    print(
                        f"""
                    {s.get('date')} {s.get('description')}
                    {s.get('from')} -> {s.get('to')}
                    Сумма: {s.get('amount')} {s.get('currency_name')}
                    """
                    )
            else:
                print(
                    """Программа: Не найдено ни одной транзакции,
            подходящей под ваши условия фильтрации"""
                )

        else:
            print(f"Программа: Статус операции {user_state} недоступен")

    else:
        print("Программа: Hеправильный ввод.")


# if __name__ == "__main__":
#     main()
