from flask import g, render_template
from flask.ext.login import current_user, login_required

from zerp import app
from zerp.db import db


@app.before_request
def check_is_authenticated():
    g.is_authenticated = current_user.is_authenticated()
    g.is_admin = False
    g.current_user = None

    if g.is_authenticated:
        g.current_user = current_user
        g.is_admin = current_user.role == 'admin'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/secret')
@login_required
def secret():
    return 'Secret <br />Name: {name}, ID: {user_id}'.format(
            name=current_user.name, user_id=current_user.id)
