import aiohttp
import asyncio


async def get_status(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response.status

# Запуск асинхронной функции
# print(asyncio.run(get_status("http://example.com")))
