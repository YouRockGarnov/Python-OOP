import asyncio
from functools import wraps
import time


def async_measure_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper


@async_measure_time
async def slow_function(duration):
    await asyncio.sleep(duration)
    return duration
