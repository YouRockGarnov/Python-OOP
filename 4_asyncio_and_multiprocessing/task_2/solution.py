import asyncio


async def async_counter(start):
    while start >= 0:
        print(start)
        await asyncio.sleep(1)
        start -= 1
