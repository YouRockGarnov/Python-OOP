import pytest

from get_status import get_status


@pytest.mark.asyncio
async def test_get_status():
    result = await get_status("http://example.com")
    assert result == 200
