import asyncio


async def sum_sublist(sublist):
    return sum(sublist)


async def sum_list(numbers):
    tasks = [sum_sublist(numbers[i:i+5]) for i in range(0, len(numbers), 5)]
    results = await asyncio.gather(*tasks)
    return sum(results)


def main(numbers):
    return asyncio.run(sum_list(numbers))
