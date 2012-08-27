from flask import g
from flask.ext.login import current_user

from zerp import app


@app.before_request
def check_is_authenticated():
    g.is_authenticated = current_user.is_authenticated()

    if g.is_authenticated:
        g.current_user = current_user
        g.is_admin = current_user.role == 'admin'
