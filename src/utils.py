import json


def get_transactions(path: str) -> list | bool:
    """Функция принимает путь до JSON-файла и возвращает список словарей с данными о транзакциях"""

    try:
        with open(path) as file_with_transactions:
            try:
                transactions_list = json.load(file_with_transactions)
                if type(transactions_list) == list:
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


if __name__ == "__main__":
    path = "../data/operations.json"
    print(get_transactions(path))
