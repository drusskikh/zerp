from flask.ext.mongokit import MongoKit, Document

from zerp import app


db = MongoKit(app)


@db.register
class User(Document):
    __collection__ = 'users'

    structure = {
        'name': unicode,
        'password': unicode,
        'role': unicode,
        'first_name': unicode,
        'second_name': unicode,
        'phone': unicode
    }


@db.register
class Client(Document):
    __collection__ = 'clients'

    structure = {
        'name': unicode,
        'address': [unicode],
        'phone': [unicode]
    }
