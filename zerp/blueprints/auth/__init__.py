import uuid

from flask import Blueprint
from flask.ext.tokenauth import LoginManager, UserMixin

from zerp.db import redis


bprint = Blueprint('auth', __name__)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


class User(UserMixin):
    def __init__(self, name, _id):
        self.name = name
        self._id = _id
        self.role = 'admin'

    def get_id(self):
        return unicode(self._id)

    def login(self):
        token = uuid.uuid1()
        redis.set('token:{}'.format(token), self.get_id())
        return token

    def logout(self, token):
        redis.delete('token:{}'.format(token))


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
def load_user(token):
    user_id = redis.get('token:{}'.format(token))
    if user_id:
        return USERS_BY_ID.get(int(user_id))
    return None


def authenticate(username, password):
    try:
        return USERS_BY_NAME[username]
    except KeyError:
        return None


import zerp.blueprints.auth.views
