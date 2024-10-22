#!/usr/bin/env python3

"""
**Module:** `mongo_school_query`
**Description:** Utilities for querying school data in MongoDB collections.

**Contents:**
    - `schools_by_topic`: Retrieves a list of school documents associated
    with a specific topic.

**Dependencies:**
    - `pymongo` for MongoDB interactions

**Authors:** Mohammad Omar Siddiq
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieves a cursor to school documents containing a specified topic.

    **Args:**
        `mongo_collection`: A MongoDB collection object containing school
        documents.
        `topic`: The topic value to search for within the 'topics' field
        of school documents.

    **Returns:**
        A `Cursor` object pointing to the matching school documents.
        **Note:** This is a lazy cursor, and documents are fetched upon
        iteration.

    **Example Usage:**
        ```python
    for school in schools_by_topic(my_collection, "Mathematics"):
        print(school["school_name"])

    **Raises:**
        Exception: Any exception raised by the MongoDB Python driver during
        the query operation.
    """
    documents = mongo_collection.find({"topics": topic})
    return documents
