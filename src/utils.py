import json

# import os


def get_transactions(path: str) -> list:
    """Функция принимает путь до JSON-файла и возвращает список словарей с данными о транзакциях"""

    try:
        with open(path) as file_with_transactions:
            try:
                transactions_list = json.load(file_with_transactions)
                if isinstance(transactions_list, list):
                    return transactions_list
                else:
                    print("Файл содержит не список")
                    return []
            except json.JSONDecodeError:
                print("Невозможно декодировать (преобразовать) JSON-данные")
                return []
    except FileNotFoundError:
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
