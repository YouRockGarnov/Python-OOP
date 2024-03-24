import pytest
from squares import squares_with_delay


@pytest.mark.asyncio
async def test_squares_with_delay():
    result = await squares_with_delay([1, 2, 3, 4, 5])
    assert result == [1, 4, 9, 16, 25]
