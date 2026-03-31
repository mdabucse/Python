# app/middleware/cache.py

import time
from utils.config import CACHE_TTL

# In-memory cache
cache_store = {}


def get_cache(key: str):
    if key in cache_store:
        data, expiry = cache_store[key]

        # Check if still valid
        if time.time() < expiry:
            ttl_remaining = int(expiry - time.time())
            return data, ttl_remaining

        # Expired → remove
        del cache_store[key]

    return None, 0


def set_cache(key: str, data):
    expiry = time.time() + CACHE_TTL
    cache_store[key] = (data, expiry)