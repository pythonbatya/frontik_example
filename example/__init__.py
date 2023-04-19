from frontik.app import FrontikApplication
import example.pages
from frontik.routing import FileMappingRouter


class ExampleApplication(FrontikApplication):
    def __init__(self, **settings):
        super().__init__(**settings)

    async def init(self):
        await super().init()

    def application_urls(self):
        return [
            (r'', FileMappingRouter(example.pages)),
        ]
