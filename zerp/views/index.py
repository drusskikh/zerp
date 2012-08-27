from flask import render_template, g
from flask.ext.login import login_required, current_user

from zerp import app


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
