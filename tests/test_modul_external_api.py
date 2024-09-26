from unittest.mock import patch

import pytest
import requests

from src.external_api import get_transaction_amount


def test_get_transaction_amount_in_rub_without_conversion(fixture_expected_rub_transaction: dict) -> None:
    """Тест успешного вывода amount по транзакции в RUB"""

    result = get_transaction_amount(fixture_expected_rub_transaction)
    assert result == 1000.00


def test_get_transaction_amount_in_uncommon_currency(fixture_expected_uncommon_currency_transaction: dict) -> None:
    """Тест успешной работы приложения если валюта не [USD, UER, RUB], а какая-то другая"""

    result = get_transaction_amount(fixture_expected_uncommon_currency_transaction)
    assert result is None


def test_get_transaction_amount_with_conversion_usd_to_rub(fixture_expected_usd_transaction: dict) -> None:
    """Тест конвертации суммы транзакции из USD в RUB"""

    # Замокать requests.request, чтобы он возвращал заранее определённый результат
    with patch("requests.request") as mock_request:
        # Устанавливаем замоканному объекту ожидаемый результат
        mock_response = mock_request.return_value
        mock_response.json.return_value = {"result": 93511.12}  # Предпол API возвращает такой результат конвертации

        result = get_transaction_amount(fixture_expected_usd_transaction)
        assert result == 93511.12


def test_get_transaction_amount_without_api_key_mocked(fixture_expected_usd_transaction: dict) -> None:
    """Тест с мокированием os.getenv для проверки отсутствия API_KEY"""

    # Мокаем os.getenv только в контексте модуля external_api
    with patch("src.external_api.os.getenv", return_value=None):
        with pytest.raises(ValueError, match="API_KEY не найден"):
            get_transaction_amount(fixture_expected_usd_transaction)


def test_get_transaction_amount_api_request_error(fixture_expected_usd_transaction: dict) -> None:
    """Тест для проверки обработки ошибки при запросе к API"""

    # Мокируем запрос к API, чтобы он выбрасывал ошибку
    with patch(
        "src.external_api.requests.request",
        side_effect=requests.exceptions.RequestException("Ошибка при обращении к API"),
    ):
        result = get_transaction_amount(fixture_expected_usd_transaction)

        # Проверяем, что результатом является None, когда произошла ошибка при запросе
        assert result is None
