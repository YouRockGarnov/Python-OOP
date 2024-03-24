import pytest
from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp.pytest_plugin import aiohttp_client

from handle_sleep import handle_sleep


class MyAppTestCase(AioHTTPTestCase):

    async def get_application(self):
        app = web.Application()
        app.router.add_get('/sleep', handle_sleep)
        return app

    @unittest_run_loop
    async def test_sleep(self):
        resp = await self.client.get('/sleep?seconds=1')
        assert resp.status == 200
        text = await resp.text()
        assert '{"slept_for": 1}' in text
