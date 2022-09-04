# !/usr/bin/env python3
from flask import Flask
from .blueprint.v1 import resources
from .ext import doc_swagger


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    resources.init_app(app)
    # cors.init_app(app)
    doc_swagger.init_app(app)

    return app


if __name__ == '__main__':
    create_app.run()
