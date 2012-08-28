from flask import g, render_template
from flask.ext.login import current_user, login_required

from zerp import app


@app.before_request
def check_is_authenticated():
    g.is_authenticated = current_user.is_authenticated()

    if g.is_authenticated:
        g.current_user = current_user
        g.is_admin = current_user.role == 'admin'


@app.route('/')
def index():
    if g.is_authenticated:
        return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/secret')
@login_required
def secret():
    return 'Secret <br />Name: {name}, ID: {user_id}'.format(
            name=current_user.name, user_id=current_user.id)
