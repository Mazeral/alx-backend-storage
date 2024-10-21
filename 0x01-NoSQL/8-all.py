#!/usr/bin/env python3

"""
Module for interacting with a MongoDB database.

This module provides a function to list all documents in a MongoDB collection.
"""

from pymongo import MongoClient


if __name__ == "__main__":
    def list_all(mongo_collection):
        """
        Retrieves all documents from a MongoDB collection.

        Args:
            mongo_collection (str): The name of the MongoDB collection.

        Returns:
            list: A list of documents from the MongoDB collection.
            If the collection is empty, an empty list is returned.

        Raises:
            pymongo.errors.PyMongoError: If an error occurs while connecting
            to the MongoDB database or retrieving documents.
        """

        # Retrieve all documents from the collection
        documents = mongo_collection.find()

        # Check if the collection is empty
        if documents.count() == 0:
            # Return an empty list if the collection is empty
            return []
        else:
            # Return the list of documents
            return list(documents)
