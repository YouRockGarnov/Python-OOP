from functools import reduce


def multiply_elements(numbers):
    return reduce(lambda x, y: x * y, numbers)
