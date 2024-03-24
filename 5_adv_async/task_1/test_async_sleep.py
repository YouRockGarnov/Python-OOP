import pytest
from async_sleep import sleep_for_seconds, main


@pytest.mark.asyncio
async def test_sleep_for_seconds():
    result = await sleep_for_seconds(1)
    assert result == "Slept for 1 seconds"


@pytest.mark.asyncio
async def test_main():
    result = await main()
    assert result == ["Slept for 1 seconds", "Slept for 2 seconds"]
