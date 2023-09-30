# Python Imports
from pymongo import MongoClient
from pymongo.collection import Collection

# Imports
from mongodb_api._mongodb import get_db


# Get DB From Cluster
healthHarborDB = get_db('HealthHarbor')


class HealthHarborDB:
    users_coll: Collection = healthHarborDB.get_collection("users")
    treatments_coll: Collection = healthHarborDB.get_collection("treatments")
    search_logs_coll: Collection = healthHarborDB.get_collection("search_logs")
