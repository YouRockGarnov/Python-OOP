import pytest
from my_module import sum_list  # предполагается, что ваш код находится в my_module.py


@pytest.mark.asyncio
async def test_sum_list():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = await sum_list(numbers)
    assert result == 55
