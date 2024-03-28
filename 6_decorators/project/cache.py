from functools import wraps


class Cache:
    def __init__(self):
        self.data = {}

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: Проверьте, есть ли результат в кэше

            # TODO: Если результата нет в кэше, вызовите функцию и сохраните результат

            # TODO: Верните результат
            raise NotImplementedError("Заполните эту часть кода")
        return wrapper

    def invalidate(self, func):
        # TODO: Инвалидируйте кэш для функции
        raise NotImplementedError("Заполните эту часть кода")

cache = Cache()


@cache
def slow_function(arg):
    return arg


class MyClass:
    @cache
    def method(self, arg):
        return arg


@cache
async def async_func(arg):
    return arg
