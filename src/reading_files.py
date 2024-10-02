import logging
import os
from pathlib import Path
from typing import Dict, List

import pandas as pd

# Определяем корневую директорию проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_directory = os.path.join(BASE_DIR, "logs")
log_file = os.path.join(log_directory, "get_transactions_from_csv_and_excel.log")

# Проверяем, существует ли директория logs, и создаем ее, если нет
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger_get_transactions_from_csv_and_excel = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file, "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger_get_transactions_from_csv_and_excel.addHandler(file_handler)
logger_get_transactions_from_csv_and_excel.setLevel(logging.DEBUG)


# ВАРИАНТ 1: В функции с csv использую "FOR" + можно еще использовать "itertuples".
# Это вариант решения лучше, чем использование "APPLY", если обрабатываются большие объемы данных.


def get_transactions_from_csv(file_path: Path, delimiter: str = ";") -> List[Dict]:
    """Функция для считывания финансовых операций из CSV-файла и возвращает список словарей с транзакциями.
    :param file_path: Путь к файлу CSV.
    :param delimiter: Разделитель в CSV файле (по умолчанию ';').
    :return: Список транзакций в виде словарей."""

    try:
        logger_get_transactions_from_csv_and_excel.debug("Начато открытие и считывание CSV данных")
        df = pd.read_csv(file_path, delimiter=delimiter)

        logger_get_transactions_from_csv_and_excel.debug("Начато преобразование CSV данных в dict(orient='records')")
        list_transactions_from_csv = df.to_dict(orient="records")

        result_list_transactions = []

        logger_get_transactions_from_csv_and_excel.debug(
            "Начато формирование списка словарей из CSV с 'operationAmount'"
        )
        for transaction in list_transactions_from_csv:
            result_list_transactions.append(
                {
                    "id": transaction["id"],
                    "state": transaction["state"],
                    "date": transaction["date"],
                    "operationAmount": {
                        "amount": transaction["amount"],
                        "currency": {"name": transaction["currency_name"], "code": transaction["currency_code"]},
                    },
                    "description": transaction["description"],
                    "from": transaction["from"],
                    "to": transaction["to"],
                }
            )

        logger_get_transactions_from_csv_and_excel.debug("Завершен процесс считывания и преобразования CSV-файла")
        return list_transactions_from_csv

    except FileNotFoundError:
        logger_get_transactions_from_csv_and_excel.error(f"Файл с CSV-данными не найден: {file_path}")
        return []

    except pd.errors.ParserError:
        logger_get_transactions_from_csv_and_excel.error(f"Ошибка при парсинге CSV-файла: {file_path}")
        return []

    except KeyError as info:
        logger_get_transactions_from_csv_and_excel.error(f"Отсутствует необходимая колонка в CSV-файле: {info}")
        return []


# ВАРИАНТ 2: В функции с excel использую "APPLY" и LAMBDA-функцию (НЕ ПОДХОДИТ ДЛЯ БОЛЬШИХ ОБЪЕМОВ ДАННЫХ)


def get_transactions_from_excel(file_path: Path) -> List[dict]:
    """Функция для считывания финансовых операций из Excel-файла и возвращает список словарей с транзакциями.
    :param file_path: Путь к Excel-файлу.
    :return: Список транзакций в виде словарей."""

    try:
        logger_get_transactions_from_csv_and_excel.debug("Начато открытие и считывание Excel данных")
        df = pd.read_excel(file_path)

        logger_get_transactions_from_csv_and_excel.debug(
            "Начато формирование списка словарей из Excel с 'operationAmount'"
        )
        list_transactions_from_excel = df.apply(
            lambda row: {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "operationAmount": {
                    "amount": row["amount"],
                    "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                },
                "description": row["description"],
                "from": row["from"],
                "to": row["to"],
            },
            axis=1,
        ).to_list()

        logger_get_transactions_from_csv_and_excel.debug("Завершен процесс считывания и преобразования Excel данных")
        return list_transactions_from_excel

    except FileNotFoundError:
        logger_get_transactions_from_csv_and_excel.error(f"Файл с Excel данными не найден: {file_path}")
        return []

    except KeyError as info:
        logger_get_transactions_from_csv_and_excel.error(f"Отсутствует необходимая колонка в Excel файле: {info}")
        return []


# # Пример запуска функций из тек модуля:
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
#     print(get_transactions_from_csv(csv_file_path))
#     print(get_transactions_from_excel(excel_file_path))
