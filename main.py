# Storage imports
from service.firebase_connection import FirebaseConnection
from service.normal_storage.firestore_connect import FireStoreStorage 

# views imports
from views.page_manager import PageManager


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    page_manager = PageManager()

    firebase_connection = FirebaseConnection('https://fir-withpython-9d955-default-rtdb.firebaseio.com/',
                       './authkey/google_firebase_key.json')
    fire_app = firebase_connection.connect()
    normal_storage = FireStoreStorage(fire_app)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
