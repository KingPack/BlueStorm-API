
#!/usr/bin/env python3
from flask import Flask, jsonify
from flask import Response
from .ext import database2
from .blueprint.v1 import resources
# from .ext import doc_swagger

from .models.core import PatientsModel, PatientsSchema, PharmaciesSchema, TransactionsModel, TransactionsSchema, UsersModel, PharmaciesModel, UsersSchema

#----------------------------------------------------------------------------#
# Initialize app and set config

def create_app():

    app = Flask(__name__)

    app.config['JSON_AS_ASCII'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = database2.SessionLocal()
    
    resources.init_app(app)
    # cors.init_app(app)

    return app 

#----------------------------------------------------------------------------#

if __name__ == '__main__':
    create_app.run()