from flask import request, redirect, render_template, url_for, g
from flask.ext.login import login_required, login_user, logout_user

from zerp.blueprints.auth import bprint as auth
from zerp.blueprints.auth import authenticate
from zerp.blueprints.auth.forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
            user = authenticate(request.form['username'],
                                request.form['password'])
            if user:
                login_user(user)
                return redirect(request.args.get('next') or url_for('index'))
            else:
                error_msg = 'Incorrect login or password.'
                return redirect(url_for('auth.login', error_msg=error_msg))

    else:
        g.args = request.args
        return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
