import pytest
from my_module import fetch_all  # предполагается, что ваш код находится в my_module.py


@pytest.mark.asyncio
async def test_fetch_all():
    urls = ['http://example.com', 'http://example.org']
    results = await fetch_all(urls)
    assert len(results) == 2
    assert all(result for result in results)
