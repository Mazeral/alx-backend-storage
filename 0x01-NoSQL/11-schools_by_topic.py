#!/usr/bin/env python3

if __name__ == "__main__":
    def schools_by_topic(mongo_collection, topic):
        mongo_collection.find(*topic)
