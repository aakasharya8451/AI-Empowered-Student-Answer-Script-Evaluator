import os
from redis import Redis

from utils.custom_errors import RedisConnectionError


class RedisHandler:
    def get_redis_client(self):
        """Returns a Redis client object.

        :raises RedisConnectionError: If there is an error connecting to Redis.
        """

        redis_host = os.getenv('REDIS_HOST', 'localhost')
        redis_port = os.getenv('REDIS_PORT', 6379)
        redis_db = os.getenv('REDIS_DB', 0)
        redis_password = os.getenv('REDIS_PASSWORD', None)

        try:
            with Redis(
                    host=redis_host,
                    port=redis_port,
                    db=redis_db,
                    password=redis_password,
                    decode_responses=True) as redis_client:
                redis_client.flushall()
                print('Connected to Redis')

                return redis_client
        except Exception as e:
            raise RedisConnectionError(
                f'Error connecting to Redis: {e}')