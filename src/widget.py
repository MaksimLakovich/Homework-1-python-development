from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(data: str) -> str | None:
    """Функция принимает одну строку (тип + номер карты/счета) и возвращает маску:
    Visa Platinum 7000 79** **** 6361
    Счет **4305"""

    blocks = data.rsplit(" ", 1)
    number = blocks[-1]

    if len(number) == 16:
        mask_number = get_mask_card_number(number)
        type_and_mask_number = f"{blocks[0]} {mask_number}"
        return type_and_mask_number
    elif len(number) == 20:
        mask_number = get_mask_account(number)
        type_and_mask_number = f"{blocks[0]} {mask_number}"
        return type_and_mask_number
    else:
        return None
