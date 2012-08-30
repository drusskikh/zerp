import os

from flask import g
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.model import BaseModelView
from flask.ext.admin.contrib.fileadmin import FileAdmin

from zerp import app


class IndexView(BaseView):

    def is_accessible(self):
        return g.is_admin

    @expose('/')
    def index(self):
        return self.render('index.html')

admin = Admin(app)

admin.add_view(IndexView(name='User', endpoint='db_user', category='DB'))
admin.add_view(IndexView(name='Client', endpoint='db_client', category='DB'))

path = os.path.join(os.path.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/', name='Static Files'))
