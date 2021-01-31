import flask
from flask import request, jsonify
#from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
import connexion
import logging

logging.basicConfig(level=logging.DEBUG)
app = connexion.FlaskApp(__name__, specification_dir='./swagger/', options={"swagger_ui": True})
app.add_api('swagger.yml', arguments={"title": "Stock Report Generator"})
CORS(app.app)

#app = flask.Flask(__name__)
#app.config["DEBUG"] = True
'''
SWAGGER_URL = '/api/docs'
API_URL = 'http://127.0.0.1:5000/v1/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Stock Report Application"
    }
)
app.register_blueprint(swaggerui_blueprint)
'''

#@app.route('/', methods=['GET'])
def home():
    return "<h1>Stock Analysis Report</h1><p>This page is intended for use with generating Stock Analysis " \
           "Reports based on Yahoo Finance and internal metric generation.</p>"


app.run(port=8080, host="127.0.0.1")
