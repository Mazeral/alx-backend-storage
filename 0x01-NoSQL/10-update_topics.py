#!/usr/bin/env python3


"""
**Module:** `mongo_document_updater`
**Description:** Utilities for updating documents in MongoDB collections.

**Contents:**
    - `update_topics`: Updates multiple documents in a MongoDB collection
    by adding or modifying topics.

**Dependencies:**
    - `pymongo` for MongoDB interactions

**Authors:** Mohammad Omar Siddiq
"""


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document based on the name """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
