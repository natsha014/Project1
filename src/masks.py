def get_mask_card(card_number: int | str) -> str:
    """Принимает номер карты и возвращает маску в виде ХХХХ ХХ** **** ХХХХ"""

    card = str(card_number)
    if len(card) == 16 and card.isdigit():
        return card[:4] + " " + card[4:6] + "** **** " + card[12:]
    else:
        return "Некорректный ввод"


def get_mask_account(account_number: int | str) -> str:
    """Принимает номер счета и возвращает его маску в виде **ХХХХ"""

    a = str(account_number)
    if len(a) == 20 and a.isdigit():
        return "**" + a[-4:]
    else:
        return "Некорректный ввод"
