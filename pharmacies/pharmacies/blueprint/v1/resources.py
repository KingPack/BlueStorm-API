from flask import Blueprint, Response, jsonify
from ...ext.database2 import SessionLocal
from ...models.core import *


bp = Blueprint('bluestorm_v1', __name__, url_prefix='/v1/')
db = SessionLocal()

schema_patients = PatientsSchema(many=True)
schema_pharmacies = PharmaciesSchema(many=True)
schema_users = UsersSchema(many=True)
schema_transactions = TransactionsSchema(many=True)

def init_app(app):
    app.register_blueprint(bp)
    

@bp.route('/', methods=['GET'])
def index() -> Response:
    result = '<H1> Pagina Inicial</H1>'
    
    return Response(result, status=200, mimetype='text/html')


@bp.route('/patients/', methods=['GET'])
def patients():

    query_patients = db.query(PatientsModel).all()
    json_patients = schema_patients.dump(query_patients)

    return jsonify(json_patients)


@bp.route('/pharmacies/', methods=['GET'])
def pharmacies():

    query_pharmacies = db.query(PharmaciesModel).all()
    json_pharmacies = schema_pharmacies.dump(query_pharmacies)

    return jsonify(json_pharmacies)


@bp.route('/transactions/', methods=['GET'])
def transactions():

    query_transactions = db.query(TransactionsModel).all()
    json_transactions = schema_transactions.dump(query_transactions)

    return jsonify(json_transactions)

