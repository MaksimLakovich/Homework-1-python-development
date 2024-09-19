from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Начало логирования
            time_start = datetime.now()
            log_message = f"Функция '{func.__name__}' была запущена в {time_start}\n"

            try:
                # Выполнение функции
                result = func(*args, **kwargs)
                # Завершение логирования успешного выполнения функции
                time_finish = datetime.now()
                log_message += f"Функция '{func.__name__}' успешно завершилась в {time_finish}. Результат: {result}\n"
                if filename:
                    # запись в режиме добавить ('a'), а не перезапись ('w') чтоб сохранять предыдущие логи
                    with open(filename, "w") as file:
                        file.write(log_message)
                else:
                    print(log_message)
                return result

            except Exception as error:
                # Логирование ошибки
                error_type = type(error).__name__
                log_message += (
                    f"Функция '{func.__name__}' завершилась с ошибкой: {error_type}. "
                    f"Входные параметры: {args}, {kwargs}\n"
                )
                if filename:
                    with open(filename, "w") as file:
                        file.write(log_message)
                else:
                    print(log_message)
                # Повторно выбрасываем ошибку, чтобы поведение функции не изменялось
                raise error

        return wrapper

    return decorator


# # Пример использования декоратора
# @log(filename="mylog_for_task_decorators.txt")
# def my_function(x: int | float, y: int | float) -> int | float:
#     """Функция выполняет деление"""
#
#     return x / y
#
#
# my_function(2.6, 4)
