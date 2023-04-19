import frontik.handler


class Page(frontik.handler.PageHandler):
    async def get_page(self):
        result = await self.get_url('http://www.google.com', '/')

        self.json.put({
            'res1': result.response.code,
        })
