from functools import wraps


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: Увеличьте счетчик вызовов

        # TODO: Выведите сообщение с именем функции и количеством вызовов

        # TODO: Вызовите функцию и верните результат
        raise NotImplementedError("Заполните эту часть кода")

    wrapper.calls = 0
    return wrapper


@count_calls
def greet(name):
    return f"Hello, {name}!"
