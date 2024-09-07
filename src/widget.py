from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str | None:
    """Функция принимает одну строку (тип + номер карты/счета) и возвращает маску:
    1. Visa Platinum 7000 79** **** 6361
    2. Счет **4305"""

    if not isinstance(data, str):
        raise AttributeError("Некорректный тип данных")

    blocks = data.rsplit(" ", 1)
    number = blocks[-1]

    if len(number) == 16:
        mask_number = get_mask_card_number(int(number))
        type_and_mask_number = f"{blocks[0]} {mask_number}"
        return type_and_mask_number
    elif len(number) == 20:
        mask_number = get_mask_account(int(number))
        type_and_mask_number = f"{blocks[0]} {mask_number}"
        return type_and_mask_number
    else:
        return None


def get_date(incoming_date_time: str | None) -> str | None:
    """Функция принимает на вход строку с датой в формате c "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"""

    if incoming_date_time:
        datetime_format = datetime.strptime(incoming_date_time, "%Y-%m-%dT%H:%M:%S.%f")
        changed_date_format = datetime_format.strftime("%d-%m-%Y")

        return changed_date_format

    return None
