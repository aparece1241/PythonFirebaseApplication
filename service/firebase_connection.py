import firebase_admin
from firebase_admin import credentials


# database url : https://fir-withpython-9d955-default-rtdb.firebaseio.com/

class FirebaseConnection:

    def __init__(self, database_url, credential_path):
        self.database_url = database_url
        self.credential_path = credential_path
        self.credential = None
        self.App = None
        print('successfully initialized!')

    def connect(self):
        """Connect to db using the
            given credentials"""

        self.credential = credentials.Certificate(self.credential_path)
        self.App = firebase_admin.initialize_app(self.credential, {
            'databaseURL': self.database_url
        })

        return self.App


def return_instance_con():
    instance_con = FirebaseConnection('https://fir-withpython-9d955-default-rtdb.firebaseio.com/',
                   './authkey/google_firebase_key.json')
    return instance_con


# Check if its imported or run directly
# Initialized default value
if __name__ == '__main__':
    return_instance_con()