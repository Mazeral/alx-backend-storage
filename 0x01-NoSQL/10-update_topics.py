#!/usr/bin/env python3


"""
**Module:** `mongo_document_updater`
**Description:** Utilities for updating documents in MongoDB collections.

**Contents:**
    - `update_topics`: Updates multiple documents in a MongoDB collection
    by adding or modifying topics.

**Dependencies:**
    - `pymongo` for MongoDB interactions

**Authors:** [Your Name]
**Last Updated:** [Current Date]
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates multiple documents in a MongoDB collection by matching a 'name'
    field and updating with new topics.

    **Args:**
        `mongo_collection`: A MongoDB collection object where documents will be
        updated.
        `name`: The value to match in the 'name' field of documents
        for updating.
        `topics`: A list of update operators
        (e.g., `{"$addToSet": {"topics": "TopicName"}}`) to apply to matching
        documents.

    **Warning:**
        - The `updateMany` method uses the `name` parameter as both the filter
        value and field name.
          Ensure this aligns with your MongoDB schema.
        - The `*topics` syntax passes each update operator as a separate
        argument. Ensure `topics` is a list of properly formatted update
          operators.

    **Returns:**
        The result of the `updateMany` operation, containing the number
        of matched and modified documents.

    **Raises:**
        Exception: Any exception raised by the MongoDB Python driver during the
        update operation.
    """
    mongo_collection.updateMany({name: name}, *topics)
