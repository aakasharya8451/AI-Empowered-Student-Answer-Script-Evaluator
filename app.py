import logging
from flask import Flask
from config.config_firebase import FirebaseHandler
from config.config import get_config
from routes.auth_api import auth_api
from routes.evaluate_api import evaluate_api
from routes.logout_api import logout_api
from flask_cors import CORS 
from config.config import jwt

def create_app(config_name):
    """
    Create a Flask app.

    :param config_name: Name of the configuration to use.
    :type config_name: str
    :return: Flask app instance.
    :rtype: Flask
    :raises Exception: If there is an error creating the app.
    """
    
    try:
        app = Flask(__name__)
        app.config.from_object(get_config(config_name))
        CORS(app, origins = '*')

        jwt.init_app(app)

        FirebaseHandler()

        app.register_blueprint(auth_api, url_prefix='/api/v1')
        app.register_blueprint(evaluate_api, url_prefix='/api/v1')
        app.register_blueprint(logout_api, url_prefix='/api/v1')

        return app

    except FileNotFoundError as e:
        logging.error(f'Error creating app: {str(e)}')
        raise Exception('File not found')
    except ValueError as e:
        logging.error(f'Error creating app: {str(e)}')
        raise Exception('Invalid value')
    except Exception as e:
        logging.error(f'Error creating app: {str(e)}')
        raise Exception('Error creating app')

app = create_app('production')
