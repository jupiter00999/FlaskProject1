from flask_login import UserMixin

from routes import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    telephone = db.Column(db.String(80), nullable=False)

    def __init__(self,username,password,telephone):
        self.username = username
        self.password = password
        self.telephone = telephone
        self.id = None

        def __repr__(self):
            return '<User %r>' % self.username
