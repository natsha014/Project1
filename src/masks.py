def get_mask_card(card_number: int|str) -> str:
    """Принимает номер карты и возвращает маску в виде ХХХХ ХХ** **** ХХХХ"""

    card = str(card_number)

    return card[:4] + " " + card[4:6] + "** **** " + card[12:]


def get_mask_account(account_number: int|str) -> str:
    """Принимает номер счета и возвращает его маску в виде **ХХХХ"""

    a = str(account_number)

    return "**" + a[-4:]
