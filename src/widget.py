from masks import get_mask_account, get_mask_card


def mask_account_card(account_card: str) -> str:
    """Принимает тип и номер карты или счета, возвращает строку с замаскированным номером"""
    acc_card = account_card.split()
    if "Счет" in account_card:
        mask = get_mask_account(acc_card[-1])
    else:
        mask = get_mask_card(acc_card[-1])
    return " ".join(acc_card[0:-1]) + " " + mask


def get_date(date: str) -> str:
    """Форматирует дату в 'ДД.ММ.ГГГГ'"""
    return date[8:10] + "." + date[5:7] + "." + date[:4]
