# import os
from collections import Counter
# from pathlib import Path
from typing import Dict, List

# from src.reading_files import get_transactions_from_csv, get_transactions_from_excel
# from src.utils import get_transactions


def get_categories_number(transactions_list: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Функция подсчета количества транзакций для определенных типов (категорий).
    Аргументы:
    transactions_list -- список банковских операций (словарей).
    categories -- список категорий, по которым нужно подсчитать операции.
    Возвращает:
    Словарь с категориями и количеством операций по каждой из них."""

    # Сразу проверяю передается ли в функцию список категорий ("categories"), по которым нужно посчитать транзакции.
    # Если список категорий ("categories") пустой, то формирую его из transactions_list и считаю по всем транзакциям.
    if categories:

        counted_categories = []

        for transaction in transactions_list:
            description = transaction.get("description")  # Получаем значение "description", если оно есть
            if description in categories:  # Если "description" есть и оно в списке нужных "categories" - добавляем
                counted_categories.append(transaction["description"])
        counted = Counter(counted_categories)  # Используем Counter для подсчета кол-ва операций по каждой "categories"

        return dict(counted)

    else:

        categories = []

        for transaction in transactions_list:
            description = transaction.get("description")  # Получаем значение "description", если оно есть
            if isinstance(description, str) and description.strip():  # Проверяем, что это непустая строка
                categories.append(description)
        counted = Counter(categories)

        return dict(counted)


# # ПРОВЕРКА РАБОТЫ ФУНКЦИИ С JSON, CSV И EXCEL СРАЗУ В ТЕКУЩЕМ МОДУЛЕ:
# if __name__ == "__main__":
#
#     # Путь к файлу-CSV, который у меня размещается в проекте в директории (../data/)
#     BASE_DIR = Path(__file__).resolve().parent.parent
#     csv_path = BASE_DIR / "data" / "transactions.csv"
#
#     # Путь к файлу-EXCEL, который у меня размещается на рабочем столе (..desktop/)
#     HOME_DIR = Path.home()
#     excel_path = HOME_DIR / "desktop" / "transactions_excel.xlsx"
#
#     # Путь до файла "operations.json", который лежит в директории "data" на одном уровне с "src"
#     json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
#
#     print(get_categories_number(get_transactions_from_csv(csv_path), categories=[]))
#     print(get_categories_number(get_transactions_from_excel(excel_path), categories=["Перевод организации"]))
#     print(get_categories_number(get_transactions(json_path), categories=["Открытие вклада", "Перевод организации"]))
