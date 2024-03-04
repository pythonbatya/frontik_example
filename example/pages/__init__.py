from frontik.handler import router, PageHandler


class Page(PageHandler):
    @router.get()
    async def get_page(self):
        result = await self.get_url('http://www.google.com', '/')

        self.json.put({
            'res1': result.status_code,
        })
