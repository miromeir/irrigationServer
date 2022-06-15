import redis

redis_device_on = redis.Redis(host='localhost', port=6379, db=0)
