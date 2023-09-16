# Python Imports
from flask import Flask
from flask_cors import CORS

# Imports
from routes.health_item import health_item

app = Flask(__name__)

# Services
app.register_blueprint(health_item, url_prefix="/health_item")
CORS(app)


@app.route("/")
def home() -> str:
    return 'Health Harbor APP BACKEND API :: UNAUTHORIZED ACCESS'


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5050, debug=True)
