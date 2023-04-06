from redis import Redis
from app.core.config import settings
from typing import Dict


class CacheDatabase:
    REGISTER_CACHEDB = 0
    SUBSCRIPTION_CACHEDB = 1
    USER_CACHEDB = 2


class RedisClientFactory:
    __instances: Dict[int, Redis] = {}

    @staticmethod
    def get_client(db: int) -> Redis:
        instance = RedisClientFactory.__instances.get(db)
        if not instance:
            instance = Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=db,
                password=settings.REDIS_PASSWORD,
            )
            RedisClientFactory.__instances[db] = instance
        return instance


class CacheManager:
    def __init__(self, cache_db: int):
        self.cache_db = cache_db
        self.cache_instance = RedisClientFactory.get_client(db=self.cache_db)

    def get(self, key):
        return self.cache_instance.get(key)

    def upsert(self, key, value, expire_after_seconds=None):
        return self.cache_instance.set(key, value, expire_after_seconds)

    def delete(self, key):
        return self.cache_instance.delete(key)

    def update_existing_key_name(self, old_key, new_key):
        instance_payload = self.get(old_key)
        self.delete(old_key)
        return self.upsert(key=new_key, value=instance_payload)
