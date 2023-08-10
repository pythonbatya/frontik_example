import frontik.handler
import gzip
import json


class Page(frontik.handler.PageHandler):
    # sentry_dsn = 'http://secret@127.0.0.1:9400/2'
    # sentry_dsn = 'https://secret@sentry.pyn.ru/200'
    async def post_page(self):
        message = gzip.decompress(self.request.body).decode('utf8')
        sentry_event = json.loads(message.split('\n')[-1])
        print(sentry_event)
