from flask import Blueprint, Response

bp = Blueprint('bluestorm_v1', __name__, url_prefix='/v1/')

def init_app(app):
    app.register_blueprint(bp)
    

@bp.route('/', methods=['GET'])
def index() -> Response:
    result = '<H1> Pagina Inicial</H1>'
    
    return Response(result, status=200, mimetype='text/html')


@bp.route('/patients/', methods=['GET'])
def patients() -> Response:
    result = '<H1> Dados patients</H1>'
    
    return Response(result, status=200, mimetype='text/html')


@bp.route('/pharmacies/', methods=['GET'])
def pharmacies() -> Response:
    result = '<H1> Dados pharmacies</H1>'
    
    return Response(result, status=200, mimetype='text/html')


@bp.route('/transactions/', methods=['GET'])
def transactions() -> Response:
    result = '<H1> Dados transactions </H1>'
    
    return Response(result, status=200, mimetype='text/html')

