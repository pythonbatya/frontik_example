import gzip
import json
import logging

from frontik.app import router
from frontik.handler import PageHandler, get_current_handler


# sentry_dsn = 'http://secret@127.0.0.1:9400/2'
# sentry_dsn = 'https://secret@sentry.pyn.ru/200'
@router.post('/api/2/store', cls=PageHandler)
async def post_page1(self: PageHandler = get_current_handler()):
    message = gzip.decompress(self.body_bytes).decode('utf8')
    sentry_event = json.loads(message.split('\n')[-1])
    print(sentry_event)


@router.post('/api/2/envelope/', cls=PageHandler)
async def post_page2(self: PageHandler = get_current_handler()):
    message = gzip.decompress(self.body_bytes).decode('utf8')
    print(message)
    # sentry_event = json.loads(message.split('\n')[-1])
    # print(sentry_event)
