from flask import render_template,send_from_directory
from flask import send_from_directory

from routes import app

# 路径映射
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(app.static_folder+'/css',path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('../static/js',path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('../static/img',path)

@app.route('/index')
def index2():
    return render_template('index.html')

@app.route('/login')
@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')