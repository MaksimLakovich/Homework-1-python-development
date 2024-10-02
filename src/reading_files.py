from pathlib import Path
from typing import List

import pandas as pd


def get_transactions_from_csv(file_path: Path, delimiter: str = ";") -> List[dict]:
    """Функция для считывания финансовых операций из CSV-файла и возвращает список словарей с транзакциями"""

    try:
        df = pd.read_csv(file_path, delimiter=delimiter)

        # ВАРИАНТ 1: через apply() и lambda-функцию
        list_transactions_from_csv = df.apply(
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

        # # ВАРИАНТ 2: через for
        # list_transactions_from_csv = df.to_dict(orient="records")
        # result_list_transactions = []
        # for transaction in list_transactions_from_csv:
        #     result_list_transactions.append(
        #         {
        #             "id": transaction["id"],
        #             "state": transaction["state"],
        #             "date": transaction["date"],
        #             "operationAmount": {
        #                 "amount": transaction["amount"],
        #                 "currency": {"name": transaction["currency_name"], "code": transaction["currency_code"]},
        #             },
        #             "description": transaction["description"],
        #             "from": transaction["from"],
        #             "to": transaction["to"],
        #         }
        #     )

        return list_transactions_from_csv

    except FileNotFoundError:
        print("Файл с CSV-данными не найден")
        return []


def get_transactions_from_excel(file_path: Path) -> List[dict]:
    """Функция для считывания финансовых операций из Excel-файла и возвращает список словарей с транзакциями"""

    try:
        df = pd.read_excel(file_path)

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

        return list_transactions_from_excel

    except FileNotFoundError:
        print("Excel-файл с данными не найден")
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
