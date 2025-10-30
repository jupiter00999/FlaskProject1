from pymsgbox import password

from models.user_modle import User
from routes import db


def get_user_by_username_pwd(username,pwd):
    return User.query.filter_by(username=username,password=password).first()

def get_user_by_id(id):
    return User.query.get(id)
