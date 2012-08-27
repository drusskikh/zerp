from flask import Flask

from auth import bprint as auth


app = Flask(__name__)

app.config['CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['MONGODB_DATABASE'] = 'zerp'

app.register_blueprint(auth)

from auth import login_manager
login_manager.setup_app(app)

from zerp.views import common, index
