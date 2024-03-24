import aiohttp
import asyncio


async def fetch_page(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception:
        return "Error"


async def fetch_pages(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# Запуск асинхронной функции
# urls = ["http://example.com", "http://example.org", "http://example.net"]
# print(asyncio.run(fetch_pages(urls)))
