from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='../templates',static_folder='../static')

# 配置数据库

app.config.from_object('config')
db = SQLAlchemy(app)

# 登录
login_manager = LoginManager()
login_manager.init_app(app)

from routes import views,login_route