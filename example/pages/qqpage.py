import frontik.handler
from tornado.web import HTTPError


class Page(frontik.handler.PageHandler):
    async def post_page(self):
        raise RuntimeError('qqqqq')
        # raise HTTPError(569, 'yo yo yo')
