from flask_jwt_extended import JWTManager
import sys
import os

# Add current working directory to sys path to access modules
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from config.config_redis import RedisHandler


redis_handler = RedisHandler()
redis_client = redis_handler.get_redis_client()

jwt = JWTManager()

class JWTBlocklistChecker:
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blacklist(self, decrypted_token: dict) -> bool:
        """
        Check if the given token is in Redis blocklist.

        :param jwt_header: str, JWT header
        :param decrypted_token: dict, Decrypted JWT token
        :return: bool, True if token is in blocklist, False otherwise
        """
        jti = decrypted_token["jti"]
        token_in_blacklist = redis_client.get(jti)
        return token_in_blacklist is not None