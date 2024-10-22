#!/usr/bin/env python3

if __name__ == "__main__":
    from pymongo import MongoClient

    # Step 1: Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")

    # Step 2: Access the database and collection
    db = client['logs']
    collection = db['nginx']

    # Step 3: Count total documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Step 4: Count documents by HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")

    # Step 5: Count documents with method=GET and path=/status
    status_check = collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_check} status check")
