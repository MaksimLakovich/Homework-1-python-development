import logging
import os

# Определяем корневую директорию проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_directory = os.path.join(BASE_DIR, "logs")
log_file = os.path.join(log_directory, "get_mask.log")

# Проверяем, существует ли директория logs, и создаем ее, если нет
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger_mask = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file, "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger_mask.addHandler(file_handler)
logger_mask.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str | None:
    """Функция принимает номер карты и возвращает ее маску: XXXX XX** **** XXXX"""

    number = str(card_number)
    logger_mask.info(f"На обработку поступил следующий номер карты: '{number}'")

    logger_mask.debug("Начат процесс преобразования номера карты")
    if number.isdigit() and len(number) == 16:
        card_blocks = [
            number[0:4],
            number[4:6],
            number[6:8],
            number[8:12],
            number[12:16],
        ]
        mask_card = f"{card_blocks[0]} {card_blocks[1]}** **** {card_blocks[4]}"
        logger_mask.debug("Преобразование номера карты завершено и возвращена маска")
        return mask_card
    else:
        logger_mask.error("Невозможно применить маску (ошибка в поступивших на обработку данных)")
        return None


def get_mask_account(account_number: int) -> str | None:
    """Функция принимает номер счета и возвращает его маску: **XXXX"""

    number = str(account_number)
    logger_mask.info(f"На обработку поступил следующий номер счета: '{number}'")

    logger_mask.debug("Начат процесс преобразования номера счета")
    if number.isdigit() and len(number) == 20:
        mask_account = f"**{number[-4:]}"
        logger_mask.debug("Преобразование номера счета завершено и возвращена маска")
        return mask_account
    else:
        logger_mask.error("Невозможно применить маску (ошибка в поступивших на обработку данных)")
        return None


# # Пример запуска функций в модуле для проверки работоспособности:
# print(get_mask_card_number("3232909466428820"))
# print(get_mask_account("32329094664288201234"))
