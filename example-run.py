#!/usr/bin/env python3
from frontik.server import main


# curl '127.0.0.1:9400/status'
# можно докинуть парам --port=9411
if __name__ == '__main__':
    main('./frontik.cfg')
