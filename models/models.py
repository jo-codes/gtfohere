import datetime
from . import db

class User(db.Model):
    ip = db.Column(db.String(32), primary_key=True)
    first_connect = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f'<User> {self.ip_adress}'
