import redis

from zerp.db.models import User


connection_pool = redis.ConnectionPool(max_connections=100)


def get_connection():
    return redis.Redis(connection_pool=connection_pool)


class RedisAPI(object):

    def user_create(self, values):

        User.validate(values)
        connection = get_connection()
        _id = connection.incr(User.incr())
        user = User(_id)

        with connection.pipeline() as pipe:
            while True:
                try:
                    pipe.watch(user.uindex('name'))

                    if pipe.hget(user.uindex('name'), values['name']):
                        raise Exception('Username must be unique.')

                    pipe.multi()
                    pipe.set(user.name, values['name'])
                    pipe.rpush(user.address, values.get('address'))
                    pipe.rpush(user.phone, values.get('phone'))
                    pipe.hset(user.uindex('name'), values['name'], _id)

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

        with connection.lock(user.lock(), timeout=5):

            with connection.pipeline() as pipe:

                if values.get('address'):
                    pipe.delete(user.address)
                    pipe.rpush(user.address, values['address'])

                if values.get('phone'):
                    pipe.delete(user.phone)
                    pipe.rpush(user.phone, values['phone'])

                pipe.execute()

    def user_find_by_id(self, _id):
        pass

    def user_find_by_name(self, name):
        pass
