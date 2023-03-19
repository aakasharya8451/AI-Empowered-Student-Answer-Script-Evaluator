from flask_jwt_extended import JWTManager
from datetime import datetime, timedelta

# expires = datetime.now() + timedelta(seconds=app.config["JWT_ACCESS_TOKEN_EXPIRES"])
import os
from dotenv import load_dotenv
# print(datetime.now() + timedelta(seconds=int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))))
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

jwt = JWTManager()

class Config:
    """A base configuration class.
    """
    DEBUG: bool = bool(os.environ.get('DEBUG'))
    TESTING: bool = bool(os.getenv('TESTING'))
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION: str = os.getenv('JWT_TOKEN_LOCATION')
    print(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'), type(os.getenv('JWT_ACCESS_TOKEN_EXPIRES')))
    JWT_ACCESS_TOKEN_EXPIRES: int = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    # JWT_ACCESS_TOKEN_EXPIRES: int = os.getenv('JWT_ACCESS_TOKEN_EXPIRES')



class Development(Config):
    """A configuration class for development environments.
    """
    DEBUG: bool = True


class Production(Config):
    """A configuration class for production environments.
    """
    DEBUG: bool = False


def get_config(config_name: str) -> Config:
    """Returns the configuration object for the specified environment.

    :param config_name (str): The name of the environment. Must be either 'development' or 'production'.

    :raises ValueError: If the specified environment name is invalid.

    :return: Config: The configuration object for the specified environment.
    """
    
    if config_name.lower() == 'production':
        return Production()
    elif config_name.lower() == 'development':
        return Development()
    else:
        raise ValueError(
            f"Invalid environment name: {config_name}. Must be either 'development' or 'production'.")
