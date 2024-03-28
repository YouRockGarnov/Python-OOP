from io import StringIO
import sys
from .count_calls import greet


def test_count_calls():
    # Перенаправляем стандартный вывод в строку
    out = StringIO()
    sys.stdout = out

    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"

    # Восстанавливаем стандартный вывод
    sys.stdout = sys.__stdout__

    # Проверяем вывод декоратора
    assert out.getvalue() == "Function greet was called 1 times\nFunction greet was called 2 times\n"
