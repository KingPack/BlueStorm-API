
#!/usr/bin/env python3
from flask import Flask, jsonify
from flask import Response
from .ext import database2
# from .ext import doc_swagger

from .models.core import PatientsModel, PatientsSchema 

#----------------------------------------------------------------------------#
# Initialize app and set config

def create_app():
    schema_patients = PatientsSchema(many=True)
    db = database2.SessionLocal()
    
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # cors.init_app(app)
    # resources.init_app(app)app

    @app.route('/patients/', methods=['GET'])
    def index():
        all_patients_query = db.query(PatientsModel).all()
        print(all_patients_query[0].UUID)
        all_patients_json = schema_patients.dump(all_patients_query)

        return jsonify(all_patients_json)

    return app

#----------------------------------------------------------------------------#

if __name__ == '__main__':
    create_app.run()