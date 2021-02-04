from flask_cors import CORS
import connexion
import logging

logging.basicConfig(level=logging.INFO)

host = "127.0.0.1"
port = 8080
base_swagger_url = "http://{host}:{port}/api/v1/ui".format(host=host, port=port)

def build_app():
    app = connexion.FlaskApp(__name__, specification_dir='./swagger/', options={"swagger_ui": True})
    app.add_api('swagger.yml', arguments={"title": "Stock Report Generator"})
    CORS(app.app)

    @app.route('/')
    def home():
        """
        Set a home page for the application
        :return: The rendered HTML template 'homepage.html'
        """
        with open("homepage.html", "r") as f:
            homepage = f.read()
        return homepage.format(swagger=base_swagger_url)
    return app


if __name__ == "__main__":
    app = build_app()
    app.run(port=port, host=host)
