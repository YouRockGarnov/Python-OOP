from functools import wraps


def cache(max_size):
    def decorator(func):
        cache_data = {}
        @wraps(func)
        def wrapper(*args):
            # TODO: Проверьте, есть ли результат в кэше

            # TODO: Если результата нет в кэше, вызовите функцию и сохраните результат

            # TODO: Если кэш переполнен, удалите самый старый результат

            # TODO: Верните результат
            raise NotImplementedError("Заполните эту часть кода")
        return wrapper
    return decorator


@cache(max_size=2)
def slow_function(arg):
    return arg
