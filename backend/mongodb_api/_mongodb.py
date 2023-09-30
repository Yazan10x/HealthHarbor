"""
Database Orchestrator
"""
import os
import json
from pymongo import MongoClient
from pymongo.database import Database


def get_db(database_name: str) -> Database:

    if os.environ.get('DB_URI') is not None:
        _DB_URI = os.environ.get('DB_URI')

    else:
        with open('secrets.json') as s:
            secret_json = json.load(s)
            _DB_URI = secret_json.get('DB_URI')

    _cluster: MongoClient = MongoClient(_DB_URI)
    _db: Database = _cluster[database_name]

    return _db
