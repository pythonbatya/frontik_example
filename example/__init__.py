from frontik.app import FrontikApplication
import example.pages
import example.pages.sentry
from frontik.routing import FileMappingRouter


class ExampleApplication(FrontikApplication):
    def __init__(self, **settings):
        super().__init__(**settings)

    async def init(self):
        await super().init()

    def application_urls(self):
        return [
            (r'^/api/2/store', example.pages.sentry.Page),
            (r'', FileMappingRouter(example.pages)),
        ]
