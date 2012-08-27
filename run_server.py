#!/usr/bin/env python

import sys

import eventlet
from eventlet import wsgi

from zerp import app

if len(sys.argv) == 2 and sys.argv[1] == 'eventlet':
    print 'Running eventlet server...'
    eventlet.monkey_patch()
    wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)

else:
    print 'Running werkzeug server...'
    app.run('0.0.0.0', 5000, debug=True)
