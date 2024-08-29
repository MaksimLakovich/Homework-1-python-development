def get_mask_card_number(card_number: int) -> str | None:
    """Функция принимает номер карты и возвращает ее маску: XXXX XX** **** XXXX"""

    number = str(card_number)

    if number.isdigit() and len(number) == 16:
        card_blocks = [
            number[0:4],
            number[4:6],
            number[6:8],
            number[8:12],
            number[12:16],
        ]
        return f"{card_blocks[0]} {card_blocks[1]}** **** {card_blocks[4]}"
    else:
        return None


def get_mask_account(account_number: int) -> str | None:
    """Функция принимает номер счета и возвращает его маску: **XXXX"""

    number = str(account_number)

    if number.isdigit() and len(number) == 20:
        return f"**{number[-4:]}"
    else:
        return None
