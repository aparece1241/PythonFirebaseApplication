import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
# database url : https://fir-withpython-9d955-default-rtdb.firebaseio.com/

class FirebaseConnection:

    def __init__(self, databaseUrl, credentialPath):
        self.databaseUrl = databaseUrl
        self.credentialPath = credentialPath
        print('successfully initialized!')

    def connect(self):
        """Connect to db using the
            given credentials"""


# Check if its imported or run directly
if __name__ == '__main__':
    FirebaseConnection('https://fir-withpython-9d955-default-rtdb.firebaseio.com/',
                       './authkeys/google_firebase_key.json')
