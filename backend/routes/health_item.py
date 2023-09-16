# Python Imports
import base64
from io import BytesIO

import flask
from flask import Blueprint, Response, jsonify, request, send_file

health_item = Blueprint('/health_item', __name__)


@health_item.route("/get_item/<item_id>", methods=['GET'])
def get_item(item_id: str) -> Response:
    pass


@health_item.route("/get_items", methods=['POST'])
def get_items() -> Response:
    pass


@health_item.route("/create_item", methods=['POST'])
def create_item() -> Response:
    pass


@health_item.route("/update_item", methods=['POST'])
def update_item() -> Response:
    pass


@health_item.route("/delete_item", methods=['POST'])
def delete_item() -> Response:
    pass

