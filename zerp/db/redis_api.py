import redis

from zerp.db.models import User


connection_pool = redis.ConnectionPool(max_connections=100)




def get_connection():
    return redis.Redis(connection_pool=connection_pool)


class RedisAPI(object):

    def user_create(self, values):

        User.validate(values)
        connection = get_connection()
        incr_key = '{}:incr'.format(User.get_model_name())
        _id = connection.incr(incr_key)
        user = User(_id)

        with connection.pipeline() as pipe:
            while True:
                try:
                    pipe.watch(user.uindex_key('name'))

                    if pipe.hget(user.uindex_key('name'), values['name']):
                        raise Exception('Username must be unique.')

                    pipe.multi()
                    pipe.set(user.name, values.get('name'))
                    pipe.rpush(user.address, values.get('address'))
                    pipe.rpush(user.phone, values.get('phone'))
                    pipe.hset(user.uindex_key('name'), values.get('name'), _id)

                    pipe.execute()
                    break

                except redis.WatchError:
                    continue

    def user_delete(self, _id):
        pass

    def user_update(self, _id, values):
        User.validate(values)
        connection = get_connection()
        user = User(_id)

        with connection.lock('user:{_id}:lock'.format(_id=_id), timeout=1):

            with connection.pipeline() as pipe:

                if values.get('address'):
                    pipe.delete(user.address)
                    pipe.rpush(user.address, values.get('address'))

                if values.get('phone'):
                    pipe.delete(user.phone)
                    pipe.rpush(user.phone, values.get('phone'))

                pipe.execute()

    def user_find_by_id(self, _id):
        pass

    def user_find_by_name(self, name):
        pass
