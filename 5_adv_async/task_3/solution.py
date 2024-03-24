import asyncio


async def square_with_delay(n):
    await asyncio.sleep(1)
    return n * n


async def squares_with_delay(numbers):
    tasks = [square_with_delay(n) for n in numbers]
    return await asyncio.gather(*tasks)

# Запуск асинхронной функции
# print(asyncio.run(squares_with_delay([1, 2, 3, 4, 5])))
