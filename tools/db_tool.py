#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongokit import Document, Connection


db = Connection()


@db.register
class User(Document):
    __collection__ = 'users'
    __database__ = 'zerp'

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
    __database__ = 'zerp'

    structure = {
        'name': unicode,
        'address': [unicode],
        'phone': [unicode]
    }


#import ipdb; ipdb.set_trace()

db.drop_database('zerp')

user1 = db.User(
        {
            'name': u'dimon',
            'password': u'secrete',
            'role': u'admin',
            'first_name': u'Dimon',
            'second_name': u'R',
            'phone': u'1',
        })

user2 = db.User(
        {
            'name': u'anton',
            'password': u'secrete',
            'role': u'operator',
            'first_name': u'Anton',
            'second_name': u'Y',
            'phone': u'2',
        })

user3 = db.User(
        {
            'name': u'den',
            'password': u'secrete',
            'role': u'executant',
            'first_name': u'Den',
            'second_name': u'X',
            'phone': u'3',
        })

user1.validate()
user1.save()
user2.validate()
user2.save()
user3.validate()
user3.save()


client1 = db.Client(
        {
            'name': u'Olukh1',
            'address': [u'a', u'b'],
            'phone': [u'1'],
        })

client2 = db.Client(
        {
            'name': u'Olukh2',
            'address': [u'b'],
            'phone': [u'2'],
        })

client3 = db.Client(
        {
            'name': u'Olukh3',
            'address': [u'c'],
            'phone': [u'2', u'3'],
        })

client1.validate()
client1.save()
client2.validate()
client2.save()
client3.validate()
client3.save()
