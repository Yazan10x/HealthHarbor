# Python Imports
import base64
from io import BytesIO

import flask
from flask import Blueprint, Response, jsonify, request, send_file
from flask_api import status

import json

from routes.cockroach.health_items import get_item as get
from routes.cockroach.health_items import get_items as get_multiple
from routes.cockroach.health_items import create_item as create
from routes.cockroach.health_items import update_item as update
from routes.cockroach.health_items import delete_item as delete

health_item = Blueprint('/health_item', __name__)


@health_item.route("/get_item/<item_id>", methods=['GET'])
def get_item(item_id: str) -> Response:
    return get(item_id), status.HTTP_200_OK


@health_item.route("/get_items", methods=['GET'])
def get_items() -> Response:
    return get_multiple("SELECT * FROM items") , status.HTTP_200_OK


@health_item.route("/create_item", methods=['POST'])
def create_item() -> Response:

    item =  '{ "id": "35998002-7e37-443f-ab43-e4ed7517dce9", "label":"hi", "quantity":1000, "description": "htn2023"}'
    item_dict = json.loads(item)
    create(item_dict)
    return item, status.HTTP_200_OK


@health_item.route("/update_item", methods=['POST'])
def update_item() -> Response:

    item =  '{ "id": "35998002-7e37-443f-ab43-e4ed7517dce9", "label":"hello", "quantity":200, "description": "11111111"}'
    item_dict = json.loads(item)
    update(item_dict)

    # update(request.get_json())
    return item, status.HTTP_200_OK


@health_item.route("/delete_item/<item_id>", methods=['POST'])
def delete_item(item_id: str) -> Response:
    delete(item_id)
    return item_id, status.HTTP_200_OK

