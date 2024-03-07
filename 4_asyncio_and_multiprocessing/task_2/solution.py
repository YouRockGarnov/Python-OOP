import asyncio


async def factorial(n):
    if n == 0:
        return 1
    else:
        return n * await factorial(n-1)


def main(n):
    return asyncio.run(factorial(n))
