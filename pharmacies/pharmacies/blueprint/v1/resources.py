from unicodedata import name
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

@bp.route('/patients/', methods=['GET'])
@doc_swagger.swag_from('docs/patients.yaml')
def patients():
    print('passei')
    query_patients = db.query(PatientsModel).all()
    json_patients = schema_patients.dump(query_patients)
    status_code = 200
    result = json_patients
    
    db.close()
    return jsonify(result), status_code

@bp.route('/patients/<string:name>/', methods=['GET'])
@doc_swagger.swag_from('docs/patients.yaml')
def patients_filter(name):

    print('passei')
    query_patient = db.query(PatientsModel).filter(PatientsModel.FIRST_NAME.ilike(f'%{name.upper()}%')).all()
    schema_patient = PatientsSchema(many=True)
    json_patient = schema_patient.dump(query_patient)
    status_code = 200
    result = json_patient
        
    db.close()
    return jsonify(result), status_code


@bp.route('/pharmacies/', methods=['GET'])
@doc_swagger.swag_from('docs/pharmacies.yaml')
def pharmacies():

    query_pharmacies = db.query(PharmaciesModel).all()
    json_pharmacies = schema_pharmacies.dump(query_pharmacies)

    return jsonify(json_pharmacies)

@bp.route('/pharmacies/<string:pharmacie>', methods=['GET'])
@doc_swagger.swag_from('docs/pharmacies.yaml')
def pharmacies_filter(pharmacie):

    query_pharmacies = db.query(PharmaciesModel).filter(PharmaciesModel.NAME.ilike(f'%{pharmacie.upper()}%')).all()
    schema_pharmacies = PharmaciesSchema(many=True)
    json_pharmacies = schema_pharmacies.dump(query_pharmacies)
    db.close()
    return jsonify(json_pharmacies)
    


@bp.route('/transactions/', methods=['GET'])
@doc_swagger.swag_from('docs/transactions.yaml')
def transactions():

    query_transactions = db.query(TransactionsModel).all()
    json_transactions = schema_transactions.dump(query_transactions)

    return jsonify(json_transactions)

@bp.route('/transactions/<string:transaction>', methods=['GET'])
@doc_swagger.swag_from('docs/transaction.yaml')
def transaction_filter(transaction):

    query_transaction = db.query(TransactionsModel).filter(TransactionsModel.NAME.ilike(f'%{transaction.upper()}%')).all()
    schema_transaction = TransactionsSchema(many=True)
    json_transaction = schema_transactions.dump(query_transaction)
    db.close()
    return jsonify(json_transaction)

