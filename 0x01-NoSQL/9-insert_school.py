#!/usr/bin/env python3

"""module for inserting schools in MongoDB

This module provide a function which inserts a new docuemnt
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the specified MongoDB collection.

    Args:
        mongo_collection: A MongoDB collection object where the document
        will be inserted.
        **kwargs: Keyword arguments representing the document to be inserted.
            Each key-value pair will be used as a field in the document.

    Returns:
        The result of the insert operation, as per the MongoDB Python driver's
        API.
            Typically, this includes the `_id` of the inserted document and an
            `acknowledged` status.

    Raises:
        Exception: Any exception raised by the MongoDB Python driver during the
        insert operation.
    """
    return mongo_collection.insert(kwargs)
