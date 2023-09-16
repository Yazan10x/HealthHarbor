# Python Imports
import base64
from io import BytesIO

import flask
from flask import Blueprint, Response, jsonify, request, send_file

import json

from cohere_api.cohere_api import get_disease_with_medicine

cohere_blueprint = Blueprint('/cohere', __name__)


@cohere_blueprint.route("/get_medicine", methods=['POST'])
def get_medicine() -> Response:
    description = dict(request.get_json())['description']
    res = get_disease_with_medicine(description)
    return jsonify(res)
