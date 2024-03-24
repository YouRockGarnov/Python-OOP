from aiohttp import web
import asyncio


async def handle_sleep(request):
    seconds = int(request.query.get('seconds', 1))
    await asyncio.sleep(seconds)
    return web.json_response({"slept_for": seconds})

# Создание и запуск микросервиса
# app = web.Application()
# app.router.add_get('/sleep', handle_sleep)
# web.run_app(app)
