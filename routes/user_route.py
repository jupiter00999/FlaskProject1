from models.user_modle import User
from  routes import app
from flask import render_template,session,redirect,url_for,request,flash
import  controllers.user_controller as user_c

#注册
@app.route('/pai/register',methods=['POST'])
def pai_register():
    #1.接受用户注册数据（非文件域数据）
    username = request.form['username']
    password = request.form['pwd']
    telephone = request.form['tel']
    #2.若有文件数据，保存文件数据到项目目录
    #3.封装用户model实体类

    user = User(username,password,telephone)
    #4.添加到数据库
    #4.返回结果
    try:
        user_c.add_user(user)
    except Exception as e:
        print(e)
        flash('注册失败','error')
        return redirect('/register')

    return redirect('/login')

