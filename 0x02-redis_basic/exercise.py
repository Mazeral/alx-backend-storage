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
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A decorator that increments a Redis counter each time the decorated
    method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    # Protip: when defining a decorator it is useful to
    # use functool.wraps to conserve the original function’s name, docstring,
    # etc.
    # By including self as the first parameter in the wrapper function,
    # you ensure that the wrapper has access to the same instance attributes
    # and methods as the original method
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """
        The wrapper function that increments the Redis counter and
        calls the original method.

        Args:
            self: The instance of the class that the method belongs to.

        Returns:
            Any: The result of the original method call.
        """
        # Get the qualified name of the method to use as the Redis key.
        # Increment the Redis counter for the method.
        self._redis.incr(method.__qualname__)
        # Call the original method and return its result.
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator for Cache class method to track args
    """
    @wraps(method)
    def wrapper(self: Any, *args) -> str:
        """ Wraps called method and tracks its passed argument by storing
            them to redis
        """
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        output = method(self, *args)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper


def replay(method):
    """
    Replays the call history of a method from Redis logs.

    Prints the method's qualified name, number of calls, and each call's
    input arguments with corresponding output values.

    Args:
        method (object): The method whose call history is to be replayed.
                         Must have a `__qualname__` attribute.

    Notes:
        - Assumes Redis client configuration is default.
        - Expects input/output logs to be in UTF-8 encoding.
    """
    # Establish a Redis client connection (using default configuration)
    client = redis.Client()

    # Retrieve the total number of calls for the method
    calls = client.get(method.__qualname__).decode('utf-8')
    calls = int(calls) if calls else 0  # Convert to int if not empty

    # Fetch input arguments for all calls of the method
    input_key = f"{method.__qualname__}:inputs"
    inputs = [x.decode('utf-8') for x in client.lrange(input_key, 0, -1)]

    # Fetch output values for all calls of the method
    output_key = f"{method.__qualname__}:outputs"
    outputs = [y.decode('utf-8') for y in client.lrange(output_key, 0, -1)]

    # Print method call summary
    print(f"{method.__qualname__} was called {calls} times:")

    # Print each method call with inputs and outputs
    for input_str, output_str in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input_str}) -> {output_str}")


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

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
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

    def get(self, key: str, fn: Callable = None) ->\
            Optional[Union[bytes, str, int]]:
        """
        Retrieves a value from Redis by its key.

        Args:
            key (str): The key of the value to retrieve.
            fn (Callable[[bytes], Optional[Union[bytes, str, int]]], optional):
                An optional function to apply to the retrieved value. Defaults
                to None.

        Returns:
            Optional[Union[bytes, str, int]]: The retrieved value, or None if
            the key does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves a string value from Redis by its key.

        Args:
            key (str): The key of the value to retrieve.

        Returns:
            Optional[str]: The retrieved string value, or None if the key
            does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        return value.decode("utf-8")

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves an integer value from Redis by its key.

        Args:
            key (str): The key of the value to retrieve.

        Returns:
            Optional[int]: The retrieved integer value, or None if the key
            does not exist or the value cannot be converted to an integer.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        try:
            return int(value)
        except ValueError:
            return None
