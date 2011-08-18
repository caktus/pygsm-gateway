#!/usr/bin/env python
import logging

from pygsm_gateway.http import PygsmHttpServer
from pygsm_gateway.gsm import GsmPollingThread


logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

fabulaws_logger = logging.getLogger('pygsm_gateway')
fabulaws_logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    args = {
        'url': 'http://localhost:8000/backend/pygsm-gateway/',
        'url_args': {},
        'modem_args': {
            'port': '/dev/ttyACM0',
            'baudrate': '115200',
            'rtscts': '1',
            'timeout': '10',
        }
    }
    gsm_thread = GsmPollingThread(**args)
    gsm_thread.start()
    server = PygsmHttpServer(('localhost', 8080), gsm_thread.send)
    print 'Starting server, use <Ctrl-C> to stop'
    try:
        server.serve_forever()
    except:
        raise
    finally:
        gsm_thread.running = False
        gsm_thread.join()
