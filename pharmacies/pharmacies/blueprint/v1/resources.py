from flask import Blueprint, Response, jsonify
from ...ext.database import SessionLocal
from ...models.core import *
from ...ext import doc_swagger

bp = Blueprint('bluestorm_v1', __name__, url_prefix='/v1/')
db = SessionLocal()

schema_patients = PatientsSchema(many=True)
schema_pharmacies = PharmaciesSchema(many=True)
schema_users = UsersSchema(many=True)
schema_transactions = TransactionsSchema(many=True)

def init_app(app):
    app.register_blueprint(bp)
    

@bp.route('/', methods=['GET'])
def index():
    result = '<H1> Pagina Inicial</H1>'
    print(id)
    return Response(result, status=200, mimetype='text/html')


@bp.route('/patients/<name>/', methods=['GET'])
@doc_swagger.swag_from('docs/patients.yaml')
def patients(name:str):
    try:
        if name:
            query_patient = db.query(PatientsModel).filter(PatientsModel.FIRST_NAME.ilike(f'%{name.upper()}%')).all()
            schema_patient = PatientsSchema(many=True)
            json_patient = schema_patient.dump(query_patient)
            status_code = 200
            result = json_patient
        else:
            query_patients = db.query(PatientsModel).all()
            json_patients = schema_patients.dump(query_patients)
            status_code = 200
            result = json_patients
            
    except Exception as error:
        status_code = 404
        result = {
            'mensagem' : error,
            'status_code': status_code
        }

    db.close()
    return jsonify(result), status_code


@bp.route('/pharmacies/', methods=['GET'])
@doc_swagger.swag_from('docs/pharmacies.yaml')
def pharmacies():

    query_pharmacies = db.query(PharmaciesModel).all()
    json_pharmacies = schema_pharmacies.dump(query_pharmacies)

    return jsonify(json_pharmacies)


@bp.route('/transactions/', methods=['GET'])
@doc_swagger.swag_from('docs/transactions.yaml')
def transactions():

    query_transactions = db.query(TransactionsModel).all()
    json_transactions = schema_transactions.dump(query_transactions)

    return jsonify(json_transactions)

