import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="../logs/masks.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
)

logger_card = logging.getLogger("masks_card")
logger_account = logging.getLogger("masks_account")


def get_mask_card(card_number: int | str) -> str:
    """Принимает номер карты и возвращает маску в виде ХХХХ ХХ** **** ХХХХ"""
    logger_card.info("Ввод номера карты")
    card = str(card_number)
    if len(card) == 16 and card.isdigit():
        logger_card.info("Получена маска номера карты")
        return card[:4] + " " + card[4:6] + "** **** " + card[12:]
    else:
        logger_card.error("Некорректный ввод номера карты")
        return "Некорректный ввод"


def get_mask_account(account_number: int | str) -> str:
    """Принимает номер счета и возвращает его маску в виде **ХХХХ"""
    logger_account.info("Ввод номера счета")

    a = str(account_number)

    if len(a) == 20 and a.isdigit():
        logger_account.info("Получена маска номера счета")
        return "**" + a[-4:]
    else:
        logger_account.error("Некорректный ввод номера счета")
        return "Некорректный ввод"
