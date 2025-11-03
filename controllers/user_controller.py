from models.user_modle import User
from routes import db

def get_user_by_username_pwd(username,pwd):
    return User.query.filter_by(username=username,password=pwd).first()

def get_user_by_id(id):
    return User.query.get(id)

def add_user(user):
    db.session.add(user)
    db.session.commit()