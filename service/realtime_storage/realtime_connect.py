# RealTime storage
from firebase_admin import db


class RealtimeStorage:

    def __init__(self, app, reference):
        self.app = app
        self.realtime_storage = db.reference(reference)


if __name__ == '__main__':
    print('This module in not supposed to run')
