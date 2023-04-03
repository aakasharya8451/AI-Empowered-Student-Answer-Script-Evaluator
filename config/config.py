import os
from dotenv import load_dotenv


current_working_directory = os.getcwd()
load_dotenv(os.path.join(current_working_directory, '.env'))


class Config:
    """A base configuration class.
    """
    DEBUG = bool(os.environ.get('DEBUG'))
    TESTING = bool(os.getenv('TESTING'))
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION = os.getenv('JWT_TOKEN_LOCATION')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))


class Development(Config):
    """A configuration class for development environments.
    """
    DEBUG = True
    TESTING = False


class Production(Config):
    """A configuration class for production environments.
    """
    DEBUG = False
    TESTING = False


class Testing(Config):
    """A configuration class for testing environments.
    """
    DEBUG = False
    TESTING = True


class ConfigFactory:
    @staticmethod
    def get_config(config_name: str) -> Config:
        """Returns the configuration object for the specified environment.

        :param config_name (str): The name of the environment. Must be one of 'development', 'production', or 'testing'.

        :raises ValueError: If the specified environment name is invalid.

        :return: Config: The configuration object for the specified environment.
        """
        
        if config_name.lower() == 'production':
            return Production()
        elif config_name.lower() == 'development':
            return Development()
        elif config_name.lower() == 'testing':
            return Testing()
        else:
            raise ValueError(
                f"Invalid environment name: {config_name}. Must be one of 'development', 'production', or 'testing'.")
