#!/usr/bin/env python3
"""
Insert a document in Python
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection"""
    if not mongo_collection:
        return None
    new_school_id = mongo_collection.insert_one(kwargs).inserted_id
    return new_school_id
