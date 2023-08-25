# initialize flask app

from flask import Flask


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app
