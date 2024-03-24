import pytest
import asyncio

from fetch_pages import fetch_pages


@pytest.mark.asyncio
async def test_fetch_pages():
    urls = ["http://example.com", "http://example.org", "http://example.net"]
    result = await fetch_pages(urls)
    assert len(result) == 3
    for page in result:
        assert page == "Error" or '<html' in page
