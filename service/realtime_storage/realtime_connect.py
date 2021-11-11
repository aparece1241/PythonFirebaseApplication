# RealTime storage
from firebase_admin import db


class RealtimeStorage:

    def __init__(self, app):
        self.app = app

