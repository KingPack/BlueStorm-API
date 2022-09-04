from flask import Blueprint
from flask import Response
from flask import jsonify

from ...ext.database import SessionLocal
from ...ext.doc_swagger import swag_from

from ...models.core import PatientsModel
from ...models.core import PatientsSchema
from ...models.core import PharmaciesModel
from ...models.core import PharmaciesSchema
from ...models.core import TransactionsModel
from ...models.core import TransactionsSchema


bp = Blueprint('bluestorm_v1', __name__, url_prefix='/v1/')
db = SessionLocal()

schema_patients = PatientsSchema(many=True)
schema_pharmacies = PharmaciesSchema(many=True)
schema_transactions = TransactionsSchema(many=True)


def init_app(app):
    app.register_blueprint(bp)


@bp.route('/', methods=['GET'])
def index():
    result = '<H1> Pagina Inicial</H1>'
    return Response(result, status=200, mimetype='text/html')


@bp.route('/patients/', methods=['GET'])
@swag_from('docs/patients.yaml')
def patients():
    query_patients = db.query(PatientsModel).all()
    json_patients = schema_patients.dump(query_patients)
    status_code = 200
    db.close()
    return jsonify(json_patients), status_code


@bp.route('/patients/<string:name>/', methods=['GET'])
@swag_from('docs/patient.yaml')
def patients_filter(name):
    query_patient = db.query(PatientsModel).filter(
        PatientsModel.FIRST_NAME.ilike(f'%{name.upper()}%')).all()

    json_patient = schema_patients.dump(query_patient)
    status_code = 200
    db.close()
    return jsonify(json_patient), status_code


@bp.route('/pharmacies/', methods=['GET'])
@swag_from('docs/pharmacies.yaml')
def pharmacies():
    query_pharmacies = db.query(PharmaciesModel).all()
    json_pharmacies = schema_pharmacies.dump(query_pharmacies)
    db.close()
    return jsonify(json_pharmacies)


@bp.route('/pharmacies/<string:pharmacie>', methods=['GET'])
@swag_from('docs/pharmacie.yaml')
def pharmacies_filter(pharmacie):
    query_pharmacies = db.query(PharmaciesModel).filter(
        PharmaciesModel.NAME.ilike(f'%{pharmacie.upper()}%')).all()

    json_pharmacies = schema_pharmacies.dump(query_pharmacies)
    db.close()
    return jsonify(json_pharmacies)


@bp.route('/transactions/', methods=['GET'])
@swag_from('docs/transactions.yaml')
def transactions():
    query_transactions = db.query(TransactionsModel).all()
    json_transactions = schema_transactions.dump(query_transactions)
    db.close()
    return jsonify(json_transactions)


@bp.route('/transactions/<string:transaction>', methods=['GET'])
@swag_from('docs/transaction.yaml')
def transaction_filter(transaction):
    query_transaction = db.query(TransactionsModel).filter(
        TransactionsModel.NAME.ilike(f'%{transaction.upper()}%')).all()
    json_transaction = schema_transactions.dump(query_transaction)

    for transaction in query_transaction:
        ...

    db.close()
    return jsonify(json_transaction)
