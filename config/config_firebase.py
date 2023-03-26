from firebase_admin import credentials, initialize_app, firestore
import sys
import os
from dotenv import load_dotenv
current_working_directory = os.getcwd()
load_dotenv(os.path.join(current_working_directory, '.env'))
sys.path.insert(0, current_working_directory)

# Add current working directory to sys path to access modules
from utils.custom_errors import FirebaseConnectionError


class FirebaseHandler:
    def __init__(self) -> None:
        """Initializes a new instance of the FirebaseHandler class.

        :raises FirebaseConnectionError: If there is an error connecting to Firebase.
        """

        try:
            cred = credentials.Certificate(os.path.join(
                current_working_directory, os.getenv('FIREBASE_CREDENTIALS')))
            self.firebase = initialize_app(cred)
            print('Connected to Firebase Firestore')
            
        except Exception as e:
            raise FirebaseConnectionError(
                f'Error connecting to Firebase Firestore: {e}')
