#!/usr/bin/env python3
"""
Change school topics

"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Update the topics of a school document based on the name"""
    if not mongo_collection:
        return
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
