import redis


class Redis(object):

    def __init__(self, host='localhost', port=6379, database=0, expire=86400):
        super(Redis, self).__init__()
        self.expire = int(expire)
        self.client = redis.StrictRedis(host, int(port), int(database))

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value):
        self.client.setex(key, self.expire, value)
