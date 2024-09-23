import os
from typing import Any
from unittest.mock import Mock, patch

import pytest
import requests

from src.external_api import get_transaction_amount


def test_get_transaction_amount_in_rub_without_conversion() -> None:
    """Тест успешного получения из operations.json транзакции в RUB и вывод amount"""

    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    result = get_transaction_amount(PATH_TO_FILE)
    assert next(result) == 31957.58


def test_get_transaction_amount_with_conversion_usd_to_rub(
    fixture_expected_usd_transaction: list[dict[str, Any]]
) -> None:
    """Тест конвертации суммы транзакции из USD в RUB"""

    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")

    # Мокируем get_transactions, чтобы вернуть фикстуру с транзакцией в USD
    with patch("src.external_api.get_transactions") as mock_get_transactions:
        mock_get_transactions.return_value = fixture_expected_usd_transaction

        # Мокируем запрос к API для конвертации валют
        with patch("src.external_api.requests.request") as mock_request:
            mock_response = Mock()
            mock_response.json.return_value = {"result": 93511.12}  # Предположим, конвертация USD в RUB
            mock_request.return_value = mock_response

            # Вызов функции с замоканным get_transactions и API-запросом
            result = get_transaction_amount(PATH_TO_FILE)

            # Проверка, что результат равен ожидаемой сумме после конвертации
            assert next(result) == 93511.12

            # Проверка, что запрос к API был выполнен один раз
            mock_request.assert_called_once()


def test_get_transaction_amount_without_api_key_mocked() -> None:
    """Тест с мокированием os.getenv для проверки отсутствия API_KEY"""

    with patch("os.getenv", return_value=None):  # Мокаем os.getenv, чтобы API_KEY был пустым
        PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")

        with pytest.raises(ValueError, match="API_KEY не найден в переменных окружения.env"):
            list(get_transaction_amount(PATH_TO_FILE))


def test_get_transaction_amount_api_request_error(
        fixture_expected_usd_transaction: list[dict[str, Any]]
) -> None:
    """Тест для проверки обработки ошибки при запросе к API"""

    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")

    # Мокируем get_transactions, чтобы вернуть фикстуру с транзакцией в USD
    with patch("src.external_api.get_transactions") as mock_get_transactions:
        mock_get_transactions.return_value = fixture_expected_usd_transaction

        # Мокируем запрос к API, чтобы он выбрасывал ошибку
        with patch(
            "src.external_api.requests.request",
            side_effect=requests.exceptions.RequestException("Ошибка при обращении к API"),
        ):
            result = list(get_transaction_amount(PATH_TO_FILE))

            # Проверяем, что результатом является None, когда произошла ошибка при запросе
            assert result == [None]
