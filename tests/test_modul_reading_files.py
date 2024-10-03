from pathlib import Path
from unittest.mock import MagicMock, patch

import pandas as pd

from src.reading_files import get_transactions_from_csv, get_transactions_from_excel

"""ТЕСТЫ ДЛЯ ФУНКЦИИ ДЛЯ СЧИТЫВАНИЯ CSV-ФАЙЛОВ"""


@patch("pandas.read_csv")
def test_successful_get_transactions_from_csv(mock_read_csv: MagicMock) -> None:
    """Тест на успешное чтение CSV-файла"""

    # Подготовка данных
    mock_data = pd.DataFrame(
        [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    )

    # Мокаем возврат read_csv
    mock_read_csv.return_value = mock_data

    # Вызов тестируемой функции
    result = get_transactions_from_csv(Path("some_path.csv"))

    # Проверка результата
    expected_result = [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {
                "amount": 16210,
                "currency": {"name": "Sol", "code": "PEN"},
            },
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        }
    ]
    assert result == expected_result


@patch("pandas.read_csv")
def test_file_csv_not_found(mock_read_csv: MagicMock) -> None:
    """Тест для обработки ошибки при отсутствии файла"""

    # Настройка мока, чтобы сымитировать FileNotFoundError
    mock_read_csv.side_effect = FileNotFoundError

    # Вызов тестируемой функции с несуществующим файлом
    result = get_transactions_from_csv(Path("not_existent_file.csv"))

    # Проверка, что результат это пустой список как реализовано в функции
    assert result == []


@patch("pandas.read_csv")
def test_file_csv_with_parsing_error(mock_read_csv: MagicMock) -> None:
    """Тест для обработки ошибки при парсинге CSV"""

    # Настройка мока, чтобы сымитировать ошибку парсинга
    mock_read_csv.side_effect = pd.errors.ParserError

    # Вызов тестируемой функции
    result = get_transactions_from_csv(Path("parsel_error_file.csv"))

    # Проверка, что результат это пустой список как реализовано в функции
    assert result == []


@patch("pandas.read_csv")
def test_file_csv_with_column_error(mock_read_csv: MagicMock) -> None:
    """Тест для обработки ошибки при отсутствии необходимых колонок"""

    # Подготовка данных с отсутствующей колонкой
    mock_data = pd.DataFrame(
        [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                # Отсутствует колонка "currency_name"
                "amount": 16210,
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    )

    # Мокаем возврат read_csv
    mock_read_csv.return_value = mock_data

    # Вызов тестируемой функции
    result = get_transactions_from_csv(Path("some_path.csv"))

    # Проверка, что результат это пустой список из-за отсутствия необходимых колонок как реализовано в функции
    assert result == []


"""ТЕСТЫ ДЛЯ ФУНКЦИИ ДЛЯ СЧИТЫВАНИЯ EXCEL-ФАЙЛОВ"""


@patch("pandas.read_excel")
def test_successful_get_transactions_from_excel(mock_read_excel: MagicMock) -> None:
    """Тест на успешное чтение EXCEL-файла"""

    # Подготовка данных
    mock_data = pd.DataFrame(
        [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    )

    # Мокаем возврат read_excel
    mock_read_excel.return_value = mock_data

    # Вызов тестируемой функции
    result = get_transactions_from_excel(Path("some_path.xls"))

    # Проверка результата
    expected_result = [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {
                "amount": 16210,
                "currency": {"name": "Sol", "code": "PEN"},
            },
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        }
    ]
    assert result == expected_result


@patch("pandas.read_excel")
def test_file_excel_not_found(mock_read_excel: MagicMock) -> None:
    """Тест для обработки ошибки при отсутствии файла"""

    # Настройка мока, чтобы сымитировать FileNotFoundError
    mock_read_excel.side_effect = FileNotFoundError

    # Вызов тестируемой функции с несуществующим файлом
    result = get_transactions_from_excel(Path("not_existent_file.xls"))

    # Проверка, что результат это пустой список как реализовано в функции
    assert result == []


@patch("pandas.read_excel")
def test_file_excel_with_column_error(mock_read_excel: MagicMock) -> None:
    """Тест для обработки ошибки при отсутствии необходимых колонок"""

    # Подготовка данных с отсутствующей колонкой
    mock_data = pd.DataFrame(
        [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                # Отсутствует колонка "currency_name"
                "amount": 16210,
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    )

    # Мокаем возврат read_excel
    mock_read_excel.return_value = mock_data

    # Вызов тестируемой функции
    result = get_transactions_from_excel(Path("some_path.xls"))

    # Проверка, что результат это пустой список из-за отсутствия необходимых колонок как реализовано в функции
    assert result == []
