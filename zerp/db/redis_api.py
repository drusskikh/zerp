import redis

from zerp.db.models import User


connection_pool = redis.ConnectionPool(max_connections=100)


def validate_values(model_cls, values):
    pass


def get_connection():
    return redis.Redis(connection_pool=connection_pool)


class RedisAPI(object):

    def user_create(self, values):

        validate_values(User, values)
        connection = get_connection()
        incr_key = '{}:incr'.format(User.get_model_name())
        _id = connection.incr(incr_key)
        user = User(_id)

        with connection.pipeline() as pipe:
            while True:
                try:
                    pipe.watch(user.index_key('name'))

                    if pipe.hget(user.index_key('name'), values['name']):
                        raise Exception('Username must be unique.')

                    pipe.multi()
                    pipe.set(user.name.key(), values['name'])
                    pipe.rpush(user.address.key(), values['address'])
                    pipe.rpush(user.phone.key(), values['phone'])
                    pipe.hset(user.index_key('name'),
                              values['name'],
                              unicode(_id))

                    pipe.execute()
                    break

                except redis.WatchError:
                    continue

    def user_delete(self, _id):
        pass

    def user_update(self, _id, values):
        validate_values(User, values)
        connection = get_connection()
        user = User(_id)

        with connection.lock('user:{_id}:lock'.format(_id=_id),
                timeout=1) as lock:



    def user_find_by_id(self, _id):
        pass

    def user_find_by_name(self, name):
        pass
