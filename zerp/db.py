from flask.ext.mongokit import MongoKit, Document, IS

from zerp import app


db = MongoKit(app)


@db.register
class User(Document):
    __collection__ = 'users'

    structure = {
        'name': unicode,
        'password': unicode,
        'role': IS(u'admin', u'operator', u'executant'),
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


@db.register
class Issue(Document):
    __collection__ = 'issues'

    structure = {
        'topic': unicode,
        'creator': User
    }

    use_autorefs = True
