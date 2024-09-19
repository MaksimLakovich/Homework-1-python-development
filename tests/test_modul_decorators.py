import pytest

from src.decorators import log


def test_positive_log_to_file() -> None:
    """Тест успешного выполнения функции с записью логов в файл"""

    @log(filename="src/mylog_for_task_decorators.txt")
    def my_divide_function(x: int | float, y: int | float) -> int | float:
        """Функция выполняет деление"""

        return x / y

    # Успешность самой функции
    result: float = my_divide_function(10, 5)
    assert result == 2.0

    # Успешность записи логов в файл
    with open("src/mylog_for_task_decorators.txt", "r", encoding="utf-8") as file:
        log_content: str = file.read()

    assert "Функция 'my_divide_function' была запущена" in log_content
    assert "Функция 'my_divide_function' успешно завершилась" in log_content
    assert "Результат: 2.0" in log_content


def test_positive_log_to_console(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест успешного выполнения функции с выводом логов в консоль"""

    @log(filename=None)
    def my_divide_function(x: int | float, y: int | float) -> int | float:
        """Функция выполняет деление"""

        return x / y

    # Успешность самой функции
    result: float = my_divide_function(10, 5)
    assert result == 2

    # Вывод логов в консоль
    captured_log_to_consol = capsys.readouterr()
    assert "Функция 'my_divide_function' была запущена" in captured_log_to_consol.out
    assert "Функция 'my_divide_function' успешно завершилась" in captured_log_to_consol.out
    assert "Результат: 2" in captured_log_to_consol.out


def test_error_log_to_file() -> None:
    """Тест возбуждения исключения с записью логов в файл"""

    @log(filename="src/mylog_for_task_decorators.txt")
    def my_divide_function(x: int | float, y: int | float) -> int | float:
        """Функция выполняет деление"""

        return x / y

    # Возбуждение исключения
    with pytest.raises(ZeroDivisionError):
        my_divide_function(10, 0)

    # Успешность записи логов в файл
    with open("src/mylog_for_task_decorators.txt", "r", encoding="utf-8") as file:
        log_content: str = file.read()

    assert "Функция 'my_divide_function' была запущена" in log_content
    assert "Функция 'my_divide_function' завершилась с ошибкой: ZeroDivisionError" in log_content
    assert "Входные параметры: (10, 0), {}" in log_content


def test_error_log_to_console(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест возбуждения исключения с выводом логов в консоль"""

    @log(filename=None)
    def my_divide_function(x: int | float, y: int | float) -> int | float:
        """Функция выполняет деление"""

        return x / y

    # Возбуждение исключения
    with pytest.raises(ZeroDivisionError):
        my_divide_function(10, 0)

    # Вывод логов в консоль
    captured_log_to_consol = capsys.readouterr()
    assert "Функция 'my_divide_function' была запущена" in captured_log_to_consol.out
    assert "Функция 'my_divide_function' завершилась с ошибкой: ZeroDivisionError" in captured_log_to_consol.out
    assert "Входные параметры: (10, 0), {}" in captured_log_to_consol.out
