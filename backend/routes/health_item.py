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
    item_json = request.get_json()
    create(item_json)
    return item_json, status.HTTP_200_OK


@health_item.route("/update_item", methods=['POST'])
def update_item() -> Response:
    item_json = request.get_json()
    update(item_json)
    return item_json, status.HTTP_200_OK


@health_item.route("/delete_item/<item_id>", methods=['POST'])
def delete_item(item_id: str) -> Response:
    delete(item_id)
    return item_id, status.HTTP_200_OK