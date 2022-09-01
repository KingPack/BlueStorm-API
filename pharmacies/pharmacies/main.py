
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
    schema_patients = PatientsSchema(many=True)
    schema_pharmacies = PharmaciesSchema(many=True)
    schema_users = UsersSchema(many=True)
    schema_transactions = TransactionsSchema(many=True)
    
    
    app = Flask(__name__)
    resources.init_app(app)

    # cors.init_app(app)
    app.config['JSON_AS_ASCII'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = database2.SessionLocal()
    


    return app 

#----------------------------------------------------------------------------#

if __name__ == '__main__':
    create_app.run()