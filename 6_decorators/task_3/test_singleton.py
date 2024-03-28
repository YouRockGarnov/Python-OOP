from .singleton import MyClass


def test_singleton():
    a = MyClass()
    b = MyClass()
    assert a is b
