#!/usr/bin/env python

import sys
import subprocess

from zerp import app


subprocess.call(['/usr/bin/find', 'zerp/', '-name', '*.pyc', '-delete'])

if len(sys.argv) == 2 and sys.argv[1] == 'eventlet':
    print 'Running eventlet server...'

    import eventlet
    from eventlet import wsgi

    eventlet.monkey_patch()
    wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)

elif len(sys.argv) == 2 and sys.argv[1] == 'gevent':
    print 'Running gevent server...'

    from gevent import pool as ge_pool
    from gevent import wsgi as ge_wsgi
    from gevent import monkey

    monkey.patch_all()
    pool = ge_pool.Pool()
    server=ge_wsgi.WSGIServer(('0.0.0.0', 5000), app, spawn=pool)
    server.serve_forever()

else:
    print 'Running werkzeug server...'
    app.run('0.0.0.0', 5000, debug=True)
