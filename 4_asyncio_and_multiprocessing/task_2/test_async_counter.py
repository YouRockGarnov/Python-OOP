import pytest
from unittest.mock import patch
from async_counter import async_counter


@pytest.mark.asyncio
async def test_async_counter():
    with patch('builtins.print') as mock_print:
        await async_counter(3)

    mock_print.assert_any_call(3)
    mock_print.assert_any_call(2)
    mock_print.assert_any_call(1)
    mock_print.assert_any_call(0)
