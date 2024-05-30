import asyncio

from frontik.handler import PageHandler
from frontik.handler import get_current_handler
from frontik.routing import router
from fastapi import Request


@router.get('/qqpage', cls=PageHandler)
async def get_page0(request: Request, handler: PageHandler = get_current_handler()):
    result = await handler.get_url('http://example.com', '/')

    # await asyncio.sleep(10)
    # print(f'rabotau  {result}')

    for i in range(2_000):
        handler.json.put({
            i: result.status_code,
        })

