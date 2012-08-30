from flask import g, render_template
from flask.ext.tokenauth import current_user, login_required

from zerp import app
from zerp.db import db


@app.before_request
def check_is_authenticated():
    g.is_admin = False
    g.is_authenticated = False

    if current_user:
        g.current_user = current_user
        g.is_authenticated = True
        g.is_admin = current_user.role == 'admin'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/secret')
@login_required
def secret():
    return 'Secret <br />Name: {name}, ID: {user_id}'.format(
            name=current_user.name, user_id=current_user._id)
