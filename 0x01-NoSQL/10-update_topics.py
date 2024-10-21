#!/usr/bin/env python3

if __name__ == "__main__":
    def update_topics(mongo_collection, name, topics):
        mongo_collection.updateMany({name: name}, *topics)
