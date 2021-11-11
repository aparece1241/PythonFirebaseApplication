# Firestore
from firebase_admin import firestore


class FireStoreStorage:

    def __init__(self, app):
        self.app = app
        self.storage_instance = firestore.client(self.app)

    def get_all(self, collection_name):
        collection = self.storage_instance.collection('u{collection}'.format(collection_name)).get()
        return collection


if __name__ == '__main__':
    print('This module in not supposed to run')
