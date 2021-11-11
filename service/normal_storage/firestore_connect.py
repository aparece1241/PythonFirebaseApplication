# Firestore
from firebase_admin import firestore


class FireStoreStorage:

    def __init__(self, app):
        self.app = app
