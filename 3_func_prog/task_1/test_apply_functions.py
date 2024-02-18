from apply_functions import apply_functions


def test_apply_functions():
    funcs = [lambda x: x * 2, lambda x: x + 3, lambda x: x ** 2]
    assert apply_functions(funcs, 2) == [4, 5, 4]
