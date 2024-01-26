import asyncio

from frontik.handler import PageHandler, self_getter
from frontik.app import app_router, qq_path
from fastapi import Depends, Request


class BasePage(PageHandler):
    pass


# ----------------------------------------------------------------------------------

class Page(BasePage):
    async def get_page(self):
        result = await self.get_url('http://www.google.com', '/')

        self.json.put({
            'res1': result.status_code,
        })

# ----------------------------------------------------------------------------------


# @app_router.get(qq_path())


@app_router.get('/qqpage')
async def get_version(self: Page = Depends(self_getter(Page))):
    result = await self.get_url('http://www.google.com', '/')

    self.json.put({
        'res1': result.status_code,
    })







    # self.finish('qqqq\n')
    # print(self)
    # return {123: 456}

