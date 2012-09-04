class ModelMeta(type):

    def __init__(cls, name, base, attrs):
        cls._model_name = name.lower()
        structure = attrs.get('__structure__')
        if structure:
            cls._structure = structure


class Field(object):

    def __init__(self, model_name, _id, field_name):
        self.model_name = model_name
        self._id = _id
        self.field_name = field_name

    def key(self):
        return '{model_name}:{_id}:{field_name}'.format(
            model_name=self.model_name,
            _id=self._id,
            field_name=self.field_name
        )


class Model(object):
    __metaclass__ = ModelMeta

    def __init__(self, _id):
        self._id = _id

    @classmethod
    def get_model_name(cls):
        return cls._model_name

    def __getattr__(self, name):
        if name in self._structure:
            return Field(self._model_name, self._id, name)

    def key_prefix(self):
        return '{model_name}:{_id}:'.format(model_name=self._model_name,
                                            _id=self._if)

    def index_key(self, field):
        return '{model_name}:index:{field}'.format(model_name=self._model_name,
                                                   field=field)

    def unique_index_key(self, field):
        return '{model_name}:unique_index:{field}'.format(
            model_name=self._model_name, field=field)

    def get_fields(self):
        return self._structure.keys()


class User(Model):
    __structure__ = {
        'name': unicode
        'address': list,
        'phone': list
    }


class Client(Model):
    __structure__ = {
        'name': unicode,
        'address': list,
        'phone': list
    }

