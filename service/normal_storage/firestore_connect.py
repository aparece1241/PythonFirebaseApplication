# Firestore
from firebase_admin import firestore


class FireStoreStorage:
    collection = None

    def __init__(self, app):
        self.app = app
        self.storage_instance = firestore.client(self.app)


if __name__ == '__main__':
    print('This module in not supposed to run')
