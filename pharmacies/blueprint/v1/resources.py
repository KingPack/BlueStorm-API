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

schema_patient = PatientsSchema(many=False)
schema_pharmacy = PharmaciesSchema(many=False)
schema_transaction = TransactionsSchema(many=False)


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


@bp.route('/patients/<string:name>', methods=['GET'])
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


@bp.route('/pharmacies/<string:pharmacy>', methods=['GET'])
@swag_from('docs/pharmacy.yaml')
def pharmacies_filter(pharmacy):
    query_pharmacies = db.query(PharmaciesModel).filter(
        PharmaciesModel.NAME.ilike(f'%{pharmacy.upper()}%')).all()

    json_pharmacies = schema_pharmacies.dump(query_pharmacies)
    db.close()
    return jsonify(json_pharmacies)


@bp.route('/transactions/<string:transaction>', methods=['GET'])
@swag_from('docs/transaction.yaml')
def transaction(transaction):
    query_transactions = db.query(TransactionsModel).filter(
        TransactionsModel.UUID.ilike(f'%{transaction.upper()}%')).all()
    json_transaction = schema_transactions.dump(query_transactions)
    db.close()
    return jsonify(json_transaction)


@bp.route('/transactions/', methods=['GET'])
@swag_from('docs/transactions.yaml')
def transaction_filter():

    query_transactions = db.query(
        TransactionsModel, PatientsModel, PharmaciesModel).filter(
        TransactionsModel.PATIENT_UUID == PatientsModel.UUID).filter(
        TransactionsModel.PHARMACY_UUID == PharmaciesModel.UUID).all()

    # TODO: Juntar e organizar o schema para inserir as relações
    list_transactions = []
    for transaction, patient, pharmacy in query_transactions:
        json_transaction = schema_transaction.dump(transaction)
        json_patient = schema_patient.dump(patient)
        json_pharmacy = schema_pharmacy.dump(pharmacy)

        transaction_combination = {
            'id': int(json_transaction['UUID'][4:]),
            'Transaction': json_transaction,
            'Patient': json_patient,
            'Pharmacy': json_pharmacy
            }
        list_transactions.append(transaction_combination)

    sorted(list_transactions, key=lambda id: id['id'])

    db.close()
    return jsonify(list_transactions)
