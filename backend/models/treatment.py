"""
Treatment Model

The generic term for a solution to a health problem is "treatment."
Treatment encompasses a wide range of medical interventions and strategies
aimed at alleviating or curing health issues. It can include medications,
therapies, surgeries, lifestyle changes, and other approaches designed to
improve a person's health and well-being. The specific treatment
prescribed or recommended depends on the nature of the health problem and
its underlying causes.
"""

from __future__ import annotations
from typing import Optional
from models.abstract_db_model import DB_MODEL
from bson import ObjectId
from bson.binary import Binary
from datetime import datetime


class Treatment(DB_MODEL):
    oid: ObjectId
    label: str
    quantity: int
    description: str
    image_url: str

    def __init__(self, oid: ObjectId, label: str, quantity: int, description: str, image_url: str) -> None:
        super().__init__(oid)
        self.label = str(label)
        self.quantity = quantity
        self.description = description
        self.image_url = image_url

    def to_json(self) -> dict:
        return {
            '_id': self.oid,
            'label': self.label,
            'quantity': self.quantity,
            'description': self.description,
            'image_url': self.image_url
        }

    @staticmethod
    def from_json(doc: dict) -> Treatment:
        return Treatment(
            oid=ObjectId(doc["_id"]),
            label=doc["label"],
            quantity=doc["quantity"],
            description=doc["description"],
            image_url=doc["image_url"]
        )

    def __repr__(self) -> str:
        return f'Treatment ID: {self.oid.__str__()}'
