# import os
import re

# from pathlib import Path
from typing import Dict, List

# from src.reading_files import get_transactions_from_csv, get_transactions_from_excel
# from src.utils import get_transactions


def filter_transaction_by_description(transactions_list: List[Dict], input_string: str) -> List[Dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска.
    Функция возвращает список словарей, у которых в описании есть данная строка"""

    # ВАРИАНТ 1: compile() - лучшее решение для поиска во множ.строк; escape() - безопасно экранирует любые спецсимволы
    pattern = re.compile(re.escape(input_string), flags=re.IGNORECASE)

    # # ВАРИАНТ 2: без re.compile
    # my_pattern = re.escape(search_description)

    # Вариант решения с использованием LIST COMPREHENSION
    filtered_transactions_list = [
        transaction
        for transaction in transactions_list
        if (description := transaction.get("description"))
        and isinstance(description, str)
        and description.strip()
        and pattern.search(transaction["description"])
    ]

    # # Вариант решения без LIST COMPREHENSION
    # filtered_transactions_list = []
    #
    # for transaction in transactions_list:
    #     description = transaction.get("description")  # Получаем "description", если оно есть
    #     if isinstance(description, str) and description.strip():  # Проверяем, что это непустая строка
    #         # # Для ВАРИАНТА 2, который создает паттерн без re.compile
    #         # if re.search(my_pattern, transaction["description"], flags=re.IGNORECASE):
    #         if pattern.search(transaction["description"]):
    #             filtered_transactions_list.append(transaction)

    return filtered_transactions_list


# # ПРОВЕРКА РАБОТЫ ФУНКЦИИ С JSON, CSV И EXCEL СРАЗУ В ТЕКУЩЕМ МОДУЛЕ:
# if __name__ == "__main__":
#
#     # Путь к файлу-CSV, который у меня размещается в проекте в директории (../data/)
#     BASE_DIR = Path(__file__).resolve().parent.parent
#     csv_file_path = BASE_DIR / "data" / "transactions.csv"
#
#     # Путь к файлу-EXCEL, который у меня размещается на рабочем столе (..desktop/)
#     HOME_DIR = Path.home()
#     excel_file_path = HOME_DIR / "desktop" / "transactions_excel.xlsx"
#
#     # Путь до файла "operations.json", который лежит в директории "data" на одном уровне с "src"
#     json_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
#
#     input_string = "оргАн"
#
#     print(filter_transaction_by_description(get_transactions_from_csv(csv_file_path), input_string))
#     print(filter_transaction_by_description(get_transactions_from_excel(excel_file_path), input_string))
#     print(filter_transaction_by_description(get_transactions(json_file_path), input_string))
