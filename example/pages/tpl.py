from frontik.app import router
from frontik.handler import PageHandler, get_current_handler


@router.get('/tpl', cls=PageHandler)
def get_page(self=get_current_handler()):
    self.set_template('main.html')  # This template is located in the `templates` folder
    self.json.put(
        self.get_url(self.get_header('host'), '/example')
    )
