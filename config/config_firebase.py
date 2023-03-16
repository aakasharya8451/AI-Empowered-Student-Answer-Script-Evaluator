from firebase_admin import credentials, initialize_app, firestore, delete_app, get_app
from dotenv import load_dotenv
import sys
import os
current_working_directory = os.getcwd()
sys.path.insert(0, current_working_directory)

from utils.custom_errors import FirebaseConnectionError


# class FirebaseHandler:
#     def __init__(self, name=None) -> None:
#         """Initializes a new instance of the FirebaseHandler class.

#         :raises FirebaseConnectionError: If there is an error connecting to Firebase.
#         """

#         try:
#             cred = credentials.Certificate(os.path.join(
#                 current_working_directory, os.getenv('FIREBASE_CREDENTIALS')))
#             self.firebase = initialize_app(cred, name=name)
#             self.db = firestore.client()
#             print('Connected to Firebase Firestore')
            
#         except Exception as e:
#             raise FirebaseConnectionError(
#                 f'Error connecting to Firebase Firestore: {e}')
try:
    cred = credentials.Certificate(os.path.join(
        current_working_directory, os.getenv('FIREBASE_CREDENTIALS')))
    firebase = initialize_app(cred)
    db = firestore.client()
    print('Connected to Firebase Firestore')

except Exception as e:
    raise FirebaseConnectionError(
        f'Error connecting to Firebase Firestore: {e}')
