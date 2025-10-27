import flask

from routes import app,login_manager
from flask import redirect, request, flash, session
import controllers.uer_controller   as user_c
from flask_login import login_user
@app.route('/api/login', methods=['POST'])
def appi_login():
    # 1.和获取请求数据
    username = request.form['username']
    password = request.form['pwd']

    # 2.访问数据库
    user = user_c.get_user_by_username(username, password)
    # 3.验证
    # 4.返回结果
    if user is None:
        flash("无效",'error')
        return redirect('/login')

    login_user(user)
    session['user_id'] = user.id

    return redirect('/index')



@login_manager.user_loader
def load_user(id):
    return user_c.get_user_by_id(id)