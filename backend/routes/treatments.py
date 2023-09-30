# Python Imports
import base64
from io import BytesIO

import flask
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request, send_file

from models.treatment import Treatment
from mongodb_api.health_harbor_db import HealthHarborDB

# uncomment if you want to populate the db everytime the backend starts
# from routes.cockroach.populate import populate
# populate()


treatments = Blueprint('/treatments', __name__)


@treatments.route("/get_treatment/<treatment_id>", methods=['GET'])
def get_treatment(treatment_id: str) -> Response:
    item = Treatment.from_json(HealthHarborDB.treatments_coll.find_one({'_id': ObjectId(treatment_id)})).to_json()
    item['_id'] = item['_id'].__str__()
    return jsonify(item)


@treatments.route("/get_treatment_by_label/<item_label>", methods=['GET'])
def get_item_by_label(item_label: str) -> Response:
    item = Treatment.from_json(HealthHarborDB.treatments_coll.find_one({'label': item_label})).to_json()
    item['_id'] = item['_id'].__str__()
    return jsonify(item)


@treatments.route("/get_treatments", methods=['POST'])
def get_treatments() -> Response:
    items = list(HealthHarborDB.treatments_coll.find())
    res = []
    for item in items:
        item = Treatment.from_json(item).to_json()
        item['_id'] = item['_id'].__str__()
        res.append(item)
    return jsonify(res)


@treatments.route("/create_treatment", methods=['POST'])
def create_treatment() -> Response:
    raise NotImplementedError


@treatments.route("/update_treatment", methods=['POST'])
def update_treatment() -> Response:
    raise NotImplementedError


@treatments.route("/delete_treatment/<treatment_id>", methods=['GET'])
def delete_treatment(treatment_id: str) -> Response:
    raise NotImplementedError
