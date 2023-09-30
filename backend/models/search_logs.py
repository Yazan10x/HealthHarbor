"""
search logs
"""

from __future__ import annotations
from datetime import datetime
from models.abstract_db_model import DB_MODEL
from bson import ObjectId


class SearchLog(DB_MODEL):
    oid: ObjectId
    search: dict
    res: dict
    date: datetime

    def __init__(self, oid: ObjectId, search: dict, res: dict, date: datetime) -> None:
        super().__init__(oid)
        self.search = search
        self.res = res
        self.date = date

    def to_json(self) -> dict:
        return {
            '_id': self.oid,
            'search': self.search,
            'res': self.res,
            'date': self.date
        }

    @staticmethod
    def from_json(doc: dict) -> SearchLog:
        return SearchLog(
            oid=ObjectId(doc["_id"]),
            search=doc["search"],
            res=doc["res"],
            date=doc["date"]
        )

    def __repr__(self) -> str:
        return f'Search Log ID: {self.oid.__str__()}'
