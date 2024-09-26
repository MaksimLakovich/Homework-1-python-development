import json
import logging
import os

# Определяем корневую директорию проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_directory = os.path.join(BASE_DIR, "logs")
log_file = os.path.join(log_directory, "get_transactions.log")

# Проверяем, существует ли директория logs, и создаем ее, если нет
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger_get_transactions = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file, "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger_get_transactions.addHandler(file_handler)
logger_get_transactions.setLevel(logging.DEBUG)


def get_transactions(path: str) -> list:
    """Функция принимает путь до JSON-файла и возвращает список словарей с данными о транзакциях"""

    try:
        logger_get_transactions.info(f"Запуск процесса чтения JSON-файла: '{path}'")
        with open(path) as file_with_transactions:
            try:
                transactions_list = json.load(file_with_transactions)
                if isinstance(transactions_list, list):
                    logger_get_transactions.debug("Транзакции из JSON-файла успешно прочитаны и возвращены списком")
                    return transactions_list
                else:
                    logger_get_transactions.error("Возвращен пустой список (поступивший JSON-файл содержит не список)")
                    print("Файл содержит не список")
                    return []
            except json.JSONDecodeError as info:
                logger_get_transactions.error(f"Возвращен пустой список (проблема с декодировкой: {info})")
                print("Невозможно декодировать (преобразовать) JSON-данные")
                return []
    except FileNotFoundError:
        logger_get_transactions.error("Возвращен пустой список (файл не найден)")
        print("Файл с JSON-данными не найден")
        return []


# # Пример запуска функции из тек модуля:
# if __name__ == "__main__":
#
#     # ВАРИАНТ 1 - Путь до файла "operations.json", который лежит в директории "data" на одном уровне с "src"
#     PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
#
#     # # ВАРИАНТ 2 - Используем относительный путь от текущего файла
#     # PATH_TO_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "operations.json"))
#
#     print(get_transactions(PATH_TO_FILE))
