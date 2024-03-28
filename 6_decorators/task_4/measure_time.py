import asyncio
from functools import wraps
import time


def async_measure_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # TODO: Засеките время начала выполнения функции

        # TODO: Вызовите функцию и сохраните результат

        # TODO: Засеките время окончания выполнения функции

        # TODO: Выведите сообщение с именем функции и временем ее выполнения

        # TODO: Верните результат функции
        raise NotImplementedError("Заполните эту часть кода")
    return wrapper


@async_measure_time
async def slow_function(duration):
    await asyncio.sleep(duration)
    return duration
