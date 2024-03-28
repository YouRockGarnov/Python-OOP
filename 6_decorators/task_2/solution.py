from functools import wraps
from collections import OrderedDict


def cache(max_size):
    def decorator(func):
        cache_data = OrderedDict()
        @wraps(func)
        def wrapper(*args):
            if args in cache_data:
                return cache_data[args]
            result = func(*args)
            cache_data[args] = result
            if len(cache_data) > max_size:
                cache_data.popitem(last=False)
            return result
        return wrapper
    return decorator


@cache(max_size=2)
def slow_function(arg):
    return arg
