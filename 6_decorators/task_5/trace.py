from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: Выведите сообщение перед вызовом функции

        # TODO: Вызовите функцию и сохраните результат

        # TODO: Выведите сообщение после вызова функции

        # TODO: Верните результат
        raise NotImplementedError("Заполните эту часть кода")
    return wrapper


@trace
def greet(name):
    return f"Hello, {name}!"
