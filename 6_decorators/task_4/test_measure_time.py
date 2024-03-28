import pytest
from io import StringIO
import sys
from .measure_time import slow_function


@pytest.mark.asyncio
async def test_async_measure_time():
    # Перенаправляем стандартный вывод в строку
    out = StringIO()
    sys.stdout = out

    assert await slow_function(1) == 1

    # Восстанавливаем стандартный вывод
    sys.stdout = sys.__stdout__

    # Проверяем вывод декоратора
    assert "1" in out.getvalue()
