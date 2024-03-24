import asyncio


async def sleep_for_seconds(seconds):
    await asyncio.sleep(seconds)
    return f"Slept for {seconds} seconds"


async def main():
    task1 = asyncio.create_task(sleep_for_seconds(1))
    task2 = asyncio.create_task(sleep_for_seconds(2))
    results = await asyncio.gather(task1, task2)
    return results

# Запуск асинхронной функции
# print(asyncio.run(main()))
