# test_homework.py

from .my_class import *


def test_instance_method():
    obj = MyClass(5)
    assert obj.instance_method() == "I am an instance method, my instance attribute is 5"


def test_static_method():
    assert MyClass.static_method() == "I am a static method, I don't need access to instance or class attributes"


def test_class_method():
    assert MyClass.class_method() == "I am a class method, my class attribute is I am a class attribute"


def test_str_method():
    obj = MyClass(10)
    assert str(obj) == "MyClass instance with instance attribute: 10"


def test_property_method():
    obj = MyClass(5)
    assert obj.instance_attribute_squared == 25
