from flask import Flask
from flask_jwt_extended import JWTManager
# from redis import Redis
from config.config import get_config
from routes.auth_api import auth_api
from routes.evaluate_api import evaluate_api
from routes.logout_api import logout_api
from flask_cors import CORS 

jwt = JWTManager()

# redis_client = Redis()


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
        CORS(app, origins=['http://localhost:3000'])
        jwt.init_app(app)
        # redis_client.init_app(app)

        app.register_blueprint(auth_api, url_prefix='/api/v1')
        app.register_blueprint(evaluate_api, url_prefix='/api/v1')
        app.register_blueprint(logout_api, url_prefix='/api/v1')

        return app

    except Exception as e:
        raise Exception(f'Error creating app: {str(e)}')


if __name__ == '__main__':
    try:
        app = create_app('development')
        app.run()

    except Exception as e:
        print(f'Error running app: {str(e)}')
