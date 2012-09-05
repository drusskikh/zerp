class ModelMeta(type):

    def __init__(cls, name, base, attrs):
        cls._model_name = name.lower()
        structure = attrs.get('__structure__')
        if structure:
            cls._structure = structure


class Model(object):
    __metaclass__ = ModelMeta

    def __init__(self, _id):
        self._id = _id
        self._template = self._model_name +':{}:{}'

    @classmethod
    def get_model_name(cls):
        return cls._model_name

    @classmethod
    def incr(cls):
        return '{model_name}:incr'.format(model_name=cls._model_name)

    def __getattr__(self, name):
        if name in self._structure:
            return self._template.format(self._id, name)

    def prefix(self):
        return self._template.format(self._id, '')

    def index(self, field):
        return self._template.format('index', field)

    def uindex(self, field):
        return self._template.format('uindex', field)

    def lock(self):
        return self._template.format(self._id, 'lock')

    @classmethod
    def validate(cls, values):
        pass


class User(Model):
    __structure__ = {
        'name': unicode,
        'address': list,
        'phone': list
    }


class Client(Model):
    __structure__ = {
        'name': unicode,
        'address': list,
        'phone': list
    }
