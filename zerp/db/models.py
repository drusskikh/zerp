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

    @classmethod
    def get_model_name(cls):
        return cls._model_name

    @classmethod
    def incr(cls):
        return '{model_name}:incr'.format(model_name=cls._model_name)

    def __getattr__(self, name):
        if name in self._structure:
            return '{model_name}:{_id}:{field_name}'.format(
                model_name=self._model_name,
                _id=self._id,
                field_name=name)

    def prefix(self):
        return '{model_name}:{_id}:'.format(model_name=self._model_name,
                                            _id=self._id)

    def index(self, field):
        return '{model_name}:index:{field}'.format(model_name=self._model_name,
                                                   field=field)

    def uindex(self, field):
        return '{model_name}:uindex:{field}'.format(
            model_name=self._model_name, field=field)

    def lock(self):
        return '{model_name}:{_id}:lock'.format(
            model_name=self._model_name, _id=self._id)

    def get_fields(self):
        return self._structure.keys()

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
