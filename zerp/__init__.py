from flask import Flask

app = Flask(__name__)

app.config['CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['MONGODB_DATABASE'] = 'zerp'

import zerp.db

from zerp.blueprints.auth import bprint as auth
app.register_blueprint(auth)

from zerp.blueprints.auth import login_manager
login_manager.init_app(app)

import zerp.admin
import zerp.views
