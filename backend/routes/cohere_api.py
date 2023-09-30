# Python Imports
import base64
from datetime import datetime
from io import BytesIO

import flask
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request, send_file

import json

from cohere_api.cohere_api import get_disease_with_medicine
from models.search_logs import SearchLog
from mongodb_api.health_harbor_db import HealthHarborDB

cohere_blueprint = Blueprint('/cohere', __name__)


@cohere_blueprint.route("/get_medicine", methods=['POST'])
def get_medicine() -> Response:
    search = dict(request.get_json())
    description = search['description']
    res = get_disease_with_medicine(description)
    search_log = SearchLog(ObjectId(), search=search, res={'res': res}, date=datetime.now()).to_json()
    HealthHarborDB.search_logs_coll.insert_one(search_log)
    return jsonify(res)
