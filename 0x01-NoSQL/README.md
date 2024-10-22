# 0x01-NoSQL Project

Author: **Mohammad Omar Siddiq**

## Description
This project involves various tasks related to MongoDB, focusing on database operations and scripting in both MongoDB shell and Python. The tasks include listing databases, creating databases, inserting, updating, and deleting documents, and more advanced tasks such as logging and statistics.

## Files and Tasks

### 0. List all databases
- **File**: `0-list_databases`
- **Description**: Script to list all databases in MongoDB.
- **Usage**: 
    ```bash
    mongo < 0-list_databases
    ```

### 1. Create a database
- **File**: `1-use_or_create_database`
- **Description**: Script to create or switch to a database named `my_db`.
- **Usage**: 
    ```bash
    mongo < 1-use_or_create_database
    ```

### 2. Insert document
- **File**: `2-insert`
- **Description**: Inserts a document with an attribute `name` having the value "Holberton school" into the `school` collection.
- **Usage**: 
    ```bash
    mongo my_db < 2-insert
    ```

### 3. List all documents
- **File**: `3-all`
- **Description**: Script to list all documents in the `school` collection.
- **Usage**: 
    ```bash
    mongo my_db < 3-all
    ```

### 4. All matches
- **File**: `4-match`
- **Description**: Script to list all documents with `name="Holberton school"` in the `school` collection.
- **Usage**: 
    ```bash
    mongo my_db < 4-match
    ```

### 5. Count documents
- **File**: `5-count`
- **Description**: Script to display the number of documents in the `school` collection.
- **Usage**: 
    ```bash
    mongo my_db < 5-count
    ```

### 6. Update document
- **File**: `6-update`
- **Description**: Script to update documents with `name="Holberton school"` by adding an `address` field with the value `972 Mission street`.
- **Usage**: 
    ```bash
    mongo my_db < 6-update
    ```

### 7. Delete by match
- **File**: `7-delete`
- **Description**: Script to delete all documents with `name="Holberton school"` from the `school` collection.
- **Usage**: 
    ```bash
    mongo my_db < 7-delete
    ```

### 8. List all documents in Python
- **File**: `8-all.py`
- **Description**: Python function `list_all(mongo_collection)` to list all documents in a collection. Returns an empty list if no documents are found.
- **Usage**: 
    ```python
    mongo_collection = client.my_db.school
    list_all(mongo_collection)
    ```

### 9. Insert a document in Python
- **File**: `9-insert_school.py`
- **Description**: Python function `insert_school(mongo_collection, **kwargs)` to insert a new document in the `school` collection using keyword arguments.
- **Usage**: 
    ```python
    insert_school(mongo_collection, name="UCSF", address="505 Parnassus Ave")
    ```

### 10. Change school topics
- **File**: `10-update_topics.py`
- **Description**: Python function `update_topics(mongo_collection, name, topics)` to update all topics for a school document based on the school name.
- **Usage**: 
    ```python
    update_topics(mongo_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])
    ```

### 11. Where can I learn Python?
- **File**: `11-schools_by_topic.py`
- **Description**: Python function `schools_by_topic(mongo_collection, topic)` to return a list of schools having a specific topic.
- **Usage**: 
    ```python
    schools_by_topic(mongo_collection, "Python")
    ```

### 12. Log stats
- **File**: `12-log_stats.py`
- **Description**: Python script to provide stats about Nginx logs stored in MongoDB. Displays the total number of logs and a breakdown of HTTP methods used.
- **Usage**: 
    ```bash
    python3 12-log_stats.py
    ```

## Repository
- **GitHub repository**: `alx-backend-storage`
- **Directory**: `0x01-NoSQL`

