import pytest
from my_module import factorial  # предполагается, что ваш код находится в my_module.py


@pytest.mark.asyncio
async def test_factorial():
    assert await factorial(0) == 1
    assert await factorial(1) == 1
    assert await factorial(2) == 2
    assert await factorial(3) == 6
    assert await factorial(4) == 24
