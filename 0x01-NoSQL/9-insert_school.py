#!/usr/bin/env python3

if __name__ == "__main__":
    def insert_school(mongo_collection, **kwargs):
        return mongo_collection.insert(**kwargs)
