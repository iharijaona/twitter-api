# pylint: disable=missing-docstring

from flask import Flask
from flask_restx import Api


def create_app():
    app = Flask(__name__)
    app.config['ERROR_404_HELP'] = False

    from .apis.tweets import api as tweets
    api = Api(
        app,
        version='1.0',
        title='Twitter API',
        description='A simple REST API'
    )
    api.add_namespace(tweets)

    return app
