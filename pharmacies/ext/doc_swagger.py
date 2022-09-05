from flasgger import Swagger
from flasgger import swag_from  # noqa: F401


swagger_template = {
    "swagger": '2.0',
    "openapi": '3.0',
    "operationId": "getmyData",
    "info": {
            "title": "API Farmacias",
            "description": "API de filtro de dados para farmacias.",
            "version": "1.0.0",
            'contact': {'url': "https://github.com/KingPack"},
            }
    }

swagger_config = {
    "headers": [],
    "specs": [{
        "endpoint": "/apispec_1",
        "route": '/v1_spec',
        "rule_filter": lambda rule: True,
        "model_filter": lambda tag: True,
        }
    ],
    "basePath": "/v1_spec",       # basePath == route
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/v1/documentation/",

    'swagger_ui_bundle_js': '\
        https://unpkg.com/swagger-ui-dist@3.48.0/swagger-ui-bundle.js',
    'swagger_ui_bundle_css': '\
        //unpkg.com/swagger-ui-dist@3/swagger-ui.css',
    'jquery_js': '//unpkg.com/jquery@2.2.4/dist/jquery.min.js',
    'swagger_ui_standalone_preset_js': '\
        //unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js',
    }


def init_app(app):

    app.config['SWAGGER'] = {
        'title': 'api_BlueStorm',
        'uiversion': 3,
        }

    swagger = Swagger(app, config=swagger_config,       # noqa: F841
                      template=swagger_template, validation_function=True)
