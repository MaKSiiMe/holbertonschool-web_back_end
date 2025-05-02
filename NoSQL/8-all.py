#!/usr/bin/env python3

from pymongo import MongoClient


def list_all(mongo_collection):
    """List all documents in a collection"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
