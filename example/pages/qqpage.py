import frontik.handler


class Page(frontik.handler.PageHandler):
    async def get_page(self):
        self.finish({123: 456})
