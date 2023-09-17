# Python Imports
import base64
from io import BytesIO

import flask
from flask import Blueprint, Response, jsonify, request, send_file

import json

from routes.cockroach.health_items import get_item as get
from routes.cockroach.health_items import get_item_by_label as get_by_label
from routes.cockroach.health_items import get_items as get_multiple
from routes.cockroach.health_items import create_item as create
from routes.cockroach.health_items import update_item as update
from routes.cockroach.health_items import delete_item as delete

# uncomment if you want to populate the db everytime the backend starts
# from routes.cockroach.populate import populate
# populate()


health_item = Blueprint('/health_item', __name__)


@health_item.route("/get_item/<item_id>", methods=['GET'])
def get_item(item_id: str) -> Response:
    return jsonify(get(item_id))


@health_item.route("/get_item_by_label/<item_label>", methods=['GET'])
def get_item_by_label(item_label: str) -> Response:
    return jsonify(get_by_label(item_label))


@health_item.route("/get_items", methods=['POST'])
def get_items() -> Response:
    return get_multiple(request.get_json())


@health_item.route("/create_item", methods=['POST'])
def create_item() -> Response:
    item_json = request.get_json()
    create(item_json)
    return jsonify(item_json)


@health_item.route("/update_item", methods=['POST'])
def update_item() -> Response:
    item_json = request.get_json()
    update(item_json)
    return jsonify(item_json)


@health_item.route("/delete_item/<item_id>", methods=['POST'])
def delete_item(item_id: str) -> Response:
    delete(item_id)
    return jsonify(item_id)
