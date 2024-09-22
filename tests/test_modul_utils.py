import json
from unittest.mock import mock_open, patch

from src.utils import get_transactions


def test_get_transactions_list(
    fixture_for_expected_transactions_list: list[dict], fixture_for_expected_path_file: str
) -> None:
    """Тест успешного чтения данных"""

    mock_data = json.dumps(fixture_for_expected_transactions_list)
    # Мокаем функцию open и возвращаем данные из фикстуры
    with patch("builtins.open", mock_open(read_data=mock_data)):
        # Мокаем функцию os.path.exists
        with patch("os.path.exists", return_value=True):
            transactions_list = get_transactions(fixture_for_expected_path_file)
            assert transactions_list == fixture_for_expected_transactions_list


def test_get_transactions_file_not_found(fixture_for_expected_path_file: str) -> None:
    """Тест на случай, если файл не найден"""

    # Мокаем вызов функции open, чтобы она выбросила ошибку FileNotFoundError
    with patch("builtins.open", mock_open()) as mocked_open:
        mocked_open.side_effect = FileNotFoundError  # Симулируем ошибку "файл не найден"
        transactions_list = get_transactions(fixture_for_expected_path_file)
        assert transactions_list == []  # Ожидаем пустой список


def test_get_transactions_invalid_json(fixture_for_expected_path_file: str) -> None:
    """Тест на случай, если файл содержит некорректный JSON"""

    # Мокаем функцию open, чтобы файл содержал некорректные JSON-данные
    with patch("builtins.open", mock_open(read_data="invalid json")):
        transactions_list = get_transactions(fixture_for_expected_path_file)
        assert transactions_list == []  # Ожидаем пустой список


def test_get_transactions_not_a_list(fixture_for_expected_path_file: str) -> None:
    """Тест на случай, если JSON содержит не список"""

    # Мокаем функцию open, чтобы JSON содержал не список, а другой тип данных
    mock_data = json.dumps({"not": "a list"})  # Подделываем данные, чтобы это был не список
    with patch("builtins.open", mock_open(read_data=mock_data)):
        transactions_list = get_transactions(fixture_for_expected_path_file)
        assert transactions_list == []  # Ожидаем пустой список
