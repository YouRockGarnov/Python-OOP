import pytest
from io import StringIO
import sys
from .trace import greet


def test_trace():
    # Перенаправляем стандартный вывод в строку
    out = StringIO()
    sys.stdout = out

    assert greet("Alice") == "Hello, Alice!"

    # Восстанавливаем стандартный вывод
    sys.stdout = sys.__stdout__

    # Проверяем вывод декоратора
    output = out.getvalue()
    assert "('Alice',)" in output
    assert 'greet' in output
    assert 'Hello, Alice!' in output
