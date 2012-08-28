from flask import Blueprint
from flask.ext.login import LoginManager, UserMixin


bprint = Blueprint('auth', __name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


class User(UserMixin):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.role = 'admin'


USERS_BY_NAME = {
    'dimon': User('dimon', 1),
    'anton': User('anton', 2),
    'lexa': User('lexa', 3)
}

USERS_BY_ID = {
    1: User('dimon', 1),
    2: User('anton', 2),
    3: User('lexa', 3)
}


@login_manager.user_loader
def load_user(userid):
    return USERS_BY_ID[int(userid)]


def authenticate(username, password):
    try:
        return USERS_BY_NAME[username]
    except KeyError:
        return None


import zerp.blueprints.auth.views
