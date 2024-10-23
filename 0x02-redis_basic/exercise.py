#!/usr/bin/env python3

"""
**Module:** `cache_manager`
**Description:** Simple in-memory cache manager utilizing
Redis for storing miscellaneous data.

**Contents:**
    - `Cache`: A class for interacting with the Redis cache.
        - **Initialization**: Establishes a Redis connection
        and clears the database.
        - **Data Storage**: Stores input data with a uniquely
        generated UUID key.

**Dependencies:**
    - `redis` for in-memory data storage
    - `uuid` for generating unique identifiers
"""

import redis
import uuid


class Cache:
    """
    A basic cache manager class leveraging Redis for data storage.

    **Warning:**
        - The `__init__` method clears the entire Redis database
        upon initialization.
          Use cautiously in production environments.
    """

    def __init__(self):
        """
        Initializes the Cache instance, establishing a Redis connection
        and flushing the database.

        **Note:**
            - This method clears all existing data in the Redis database.
            - Consider implementing a more nuanced database reset strategy
            for production use.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """
        Stores the provided data in Redis with a uniquely generated UUID key.

        **Args:**
            `data`: The data to be stored, supporting string, bytes, integer,
            or floating-point types.

        **Returns:**
            `uuid_key`: A string representation of the UUID used as the key
            for the stored data.

        **Example Usage:**
            ```python
        cache = Cache()
        data_to_store = "Hello, World!"
        uuid_key = cache.store(data_to_store)
        print(f"Stored data with UUID: {uuid_key}")
        """
        uuid_key = str(uuid.uuid4())
        self._redis.set(uuid_key, data)
        return uuid_key
