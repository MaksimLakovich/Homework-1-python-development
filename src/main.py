import logging
import os
from pathlib import Path

from src.filter_descriptions import filter_transaction_by_description
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reading_files import get_transactions_from_csv, get_transactions_from_excel
from src.utils import get_transactions
from src.widget import get_date, mask_account_card

# Определяю корневую директорию проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_directory = os.path.join(BASE_DIR, "logs")
log_file = os.path.join(log_directory, "main.log")

# Проверяю, существует ли директория logs, и создаю ее, если нет
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger_for_main = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file, "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger_for_main.addHandler(file_handler)
logger_for_main.setLevel(logging.DEBUG)


def main(csv_file_path: Path, excel_file_path: Path, json_file_path: str) -> None:
    """Функция для основной логики проекта по взаимодействию с пользователями.
    Связывает все реализованные функциональности между собой.
    :param csv_file_path: Путь к файлу CSV.
    :param excel_file_path: Путь к файлу EXCEL.
    :param json_file_path: Путь к файлу JSON (лучше использ. Path, а не STR, но не стал переделывать старую функцию).
    :return: Печать в консаль списка транзакция по заданным параметрам."""

    logger_for_main.debug("Запуск программы и приветствие")
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    # Выбор источника данных для анализа (файлы json, csv или excel)
    while True:
        logger_for_main.debug("Выбор источника данных для анализа (json / csv / excel)")
        user_file_selection = input("\nУкажите пункт меню: ").strip()
        if user_file_selection == "1":
            logger_for_main.debug("Выбран json файл")
            print("\nДля обработки выбран JSON-файл")
            read_file = get_transactions(json_file_path)
            break
        elif user_file_selection == "2":
            logger_for_main.debug("Выбран csv файл")
            print("\nДля обработки выбран CSV-файл")
            read_file = get_transactions_from_csv(csv_file_path)
            break
        elif user_file_selection == "3":
            logger_for_main.debug("Выбран excel файл")
            print("\nДля обработки выбран XLSX-файл")
            read_file = get_transactions_from_excel(excel_file_path)
            break
        else:
            logger_for_main.debug(f"Выбран некорректный пункт меню: '{user_file_selection}'")
            print("\nПожалуйста, укажите значение от 1 до 3")

    # Выбор статуса транзакции для фильтрации данных
    while True:
        print(
            "\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        logger_for_main.debug("Выбор статуса банковских транзакций для фильтрации данных")
        user_trans_state_selection = input("\nУкажите необходимый статус: ").upper().strip()
        if user_trans_state_selection == "EXECUTED":
            logger_for_main.debug("Транзакции отфильтрованы по EXECUTED")
            filtered_data_by_state = filter_by_state(read_file, transaction_state=user_trans_state_selection)
            print(f"\nОперации отфильтрованы по статусу '{user_trans_state_selection}'")
            break
        elif user_trans_state_selection == "CANCELED":
            logger_for_main.debug("Транзакции отфильтрованы по CANCELED")
            filtered_data_by_state = filter_by_state(read_file, transaction_state=user_trans_state_selection)
            print(f"\nОперации отфильтрованы по статусу '{user_trans_state_selection}'")
            break
        elif user_trans_state_selection == "PENDING":
            logger_for_main.debug("Транзакции отфильтрованы по PENDING")
            filtered_data_by_state = filter_by_state(read_file, transaction_state=user_trans_state_selection)
            print(f"\nОперации отфильтрованы по статусу '{user_trans_state_selection}'")
            break
        else:
            logger_for_main.debug(f"Выбран некорректный статус для фильтрации: '{user_trans_state_selection}'")
            print(f"\nСтатус операции '{user_trans_state_selection}' недоступен.")

    # Запрос дополнительной фильтрации по дате транзакции и по возрастанию/убыванию
    while True:
        print("\nОтсортировать операции по дате? Да/Нет")
        logger_for_main.debug("Доп. фильтрация по дате транзакций и формата вывода 'по убыванию'/'по возрастанию'")
        user_sort_selection_by_date = input("\nВаше решение: ").upper().strip()
        if user_sort_selection_by_date == "ДА":
            logger_for_main.debug("Положительный запрос от пользователя на фильтрацию транзакций по дате")
            print("\nОтсортировать по возрастанию или по убыванию?")
            user_sort_selection_by_order = input("\nВаше решение: ").upper().strip()
            if user_sort_selection_by_order == "ПО ВОЗРАСТАНИЮ":
                filtered_data_by_order = sort_by_date(filtered_data_by_state, sort_parameter=False)
                break
            elif user_sort_selection_by_order == "ПО УБЫВАНИЮ":
                filtered_data_by_order = sort_by_date(filtered_data_by_state, sort_parameter=True)
                break
            else:
                print("\nПожалуйста, укажите 'По возрастанию' или 'По убыванию' для дальнейшей сортировки")
        elif user_sort_selection_by_date == "НЕТ":
            logger_for_main.debug("Отказ пользователя от фильтрации транзакций по дате")
            filtered_data_by_order = filtered_data_by_state
            break
        else:
            logger_for_main.debug(f"Выбран некорректный вариант фильтрации: '{user_sort_selection_by_date}'")
            print("\nПожалуйста, укажите 'Да' или 'Нет' для сортировки операций по дате")

    # Запрос на вывод транзакций только в RUB или во всех валютах
    while True:
        print("\nВыводить только рублевые транзакции? Да/Нет")
        logger_for_main.debug("Доп. фильтрация по валюте транзакций")
        user_sort_selection_by_currency = input("\nВаше решение: ").upper().strip()
        if user_sort_selection_by_currency == "ДА":
            logger_for_main.debug("Фильтрация транзакций только в RUB")
            filtered_data_by_currency = list(filter_by_currency(filtered_data_by_order, money="RUB"))
            break
        elif user_sort_selection_by_currency == "НЕТ":
            logger_for_main.debug("Фильтрация транзакций по всем валютам")
            filtered_data_by_currency = filtered_data_by_order
            break
        else:
            logger_for_main.debug(f"Выбран некорректный вариант фильтрации: '{user_sort_selection_by_currency}'")
            print("\nПожалуйста, укажите 'Да' или 'Нет' для вывода только рублевых операций")

    # Запрос дополнительной фильтрации по определенному слову в описании транзакции (description)
    while True:
        print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет")
        logger_for_main.debug("Доп. фильтрация транзакций по определенному слову")
        user_sort_selection_by_description = input("\nВаше решение: ").upper().strip()
        if user_sort_selection_by_description == "ДА":
            input_string = input("\nВведите слово по которому выполнить фильтрацию: ").upper().strip()
            final_filtered_data = filter_transaction_by_description(filtered_data_by_currency, input_string)
            logger_for_main.debug(f"Пользователь запросил отфильтровать по '{input_string}'")
            break
        elif user_sort_selection_by_description == "НЕТ":
            logger_for_main.debug("Пользователь отказался от доп. фильтрации по слову")
            final_filtered_data = filtered_data_by_currency
            break
        else:
            logger_for_main.debug(f"Выбран некорректный вариант фильтрации: '{user_sort_selection_by_description}'")
            print("\nПожалуйста, укажите 'Да' или 'Нет' для фильтрации по определенному слову в описании")

    # ВЫВОД ИТОГА РАБОТЫ ПРОГРАММЫ
    logger_for_main.debug("Вывод итогового результата работы программы")
    print("\nРаспечатываю итоговый список транзакций...")
    if len(final_filtered_data) == 0:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"\nВсего банковских операций в выборке: {len(final_filtered_data)}")
        for transaction in final_filtered_data:
            transaction_date = get_date(transaction["date"])
            transaction_type = transaction["description"]
            transaction_amount = transaction["operationAmount"]["amount"]
            transaction_currency = transaction["operationAmount"]["currency"]["name"]
            transaction_to = mask_account_card(transaction["to"])
            # Формат вывода для "Открытие вклада" отличается от формата остальных категорий транзакций
            if transaction["description"] == "Открытие вклада":
                print(
                    f"\n{transaction_date} {transaction_type}\n"
                    f"{transaction_to}\n"
                    f"Сумма: {transaction_amount} {transaction_currency}"
                )
            else:
                transaction_from = mask_account_card(transaction["from"])
                print(
                    f"\n{transaction_date} {transaction_type}\n"
                    f"{transaction_from} -> {transaction_to}\n"
                    f"Сумма: {transaction_amount} {transaction_currency}"
                )
    logger_for_main.debug("Завершение работы программы")


# # Проверка работы функции в текущем модуле
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
#     main(csv_file_path, excel_file_path, json_file_path)
