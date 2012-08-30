from flask import Flask

app = Flask(__name__)

app.config['CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['MONGODB_DATABASE'] = 'zerp'

from zerp.blueprints.auth import bprint as auth
app.register_blueprint(auth)

from zerp.blueprints.auth import login_manager
login_manager.setup_app(app)

from zerp.blueprints.tools import bprint as tools
app.register_blueprint(tools)

import zerp.admin
import zerp.db
import zerp.views
