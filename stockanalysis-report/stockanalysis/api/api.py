import flask
from flask import request, jsonify
#from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
import connexion
import logging

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)


def build_app():
    app = connexion.FlaskApp(__name__, specification_dir='./swagger/', options={"swagger_ui": True})
    app.add_api('swagger.yml', arguments={"title": "Stock Report Generator"})
    CORS(app.app)
    return app


if __name__ == "__main__":
    app = build_app()
    app.run(port=8080, host="127.0.0.1")
