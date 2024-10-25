#!/usr/bin/env python3

"""
Module for caching web page requests.

Provides a decorator to count URL requests and cache responses.
"""

import requests
from typing import Callable
import redis
from functools import wraps


def count_urls(method: Callable) -> Callable:
    """
    Decorator to count URL requests and cache responses.

    Increments a Redis counter for each unique URL, caches the response
    for 10 seconds, and returns the cached page if available.

    Args:
        method (Callable): The method to be decorated, expected to take
            a URL as an argument and return the page content.

    Returns:
        Callable: The decorated method with URL counting and caching.
    """
    client = redis.Redis()

    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function to handle URL counting and caching.

        :param url: The URL to be requested.
        :return: The content of the web page.
        """
        # Establish a Redis client connection

        # Increment the request counter for the URL
        client.incr(f"count:{url}")

        # Check if a cached page is available
        cached_page = client.get(f"{url}")
        if cached_page:
            # Return the cached page
            return cached_page.decode('utf-8')

        # Execute the original method to fetch the page
        response = method(url)

        # Cache the response for 10 seconds
        client.set(f'{url}', response, ex=10)  # 'ex' for expiration

        return response
    return wrapper


@count_urls
def get_page(url: str) -> str:
    """
    Fetches the content of a web page.

    :param url: The URL of the web page.
    :return: The content of the web page.
    """
    # Send a GET request to the URL and return the response text
    response = requests.get(url)
    return response.text
