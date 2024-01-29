from frontik.handler import PageHandler
from fastapi import Depends, APIRouter, Request


def get_cur_handler(request: Request):
    return request.scope['handler']


def dep1():
    print('dep1')


def dep2():
    print('dep2')


async def dep3():
    print('dep3')


def dep4(handler=Depends(get_cur_handler)):
    print('dep4')


class BasePage(PageHandler):
    router = APIRouter(dependencies=[Depends(dep3), Depends(dep4)])


class Page(BasePage):
    router = BasePage.router

    @router.get("/", dependencies=[Depends(dep1), Depends(dep2)])
    async def get_page(self):
        result = await self.get_url('http://www.google.com', '/')

        self.json.put({
            'res1': result.status_code,
        })



