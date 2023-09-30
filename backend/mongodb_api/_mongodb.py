"""
Database Orchestrator
"""
import os
import json
from pymongo import MongoClient
from pymongo.database import Database


def get_db(database_name: str) -> Database:

    _DB_URI = os.environ.get('DB_URI')
    _cluster: MongoClient = MongoClient(_DB_URI)
    _db: Database = _cluster[database_name]

    return _db
