#! /usr/bin/env python3
from flask import Flask
from flask import render_template,request
from hashlib import sha1
from werkzeug.security import generate_password_hash,check_password_hash
from flask_migrate import MigrateCommand,Migrate
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = \
    'mysql+pymysql://root:123456@localhost:3306/Blog'
app.config["DEBUG"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(200),nullable=True)
    url = db.Column(db.String(200),nullable=True)
    upwd = db.Column(db.String(200),nullable=False)

db.drop_all()
db.create_all()
@app.route('/')
@app.route('/index.html')
@app.route('/index/')
@app.route('/index')
def f1():
    return render_template("index.html")

@app.route('/list.html')
@app.route('/list/')
@app.route('/list')
def f2():
    return render_template("list.html")

@app.route('/photo.html')
@app.route('/photo/')
@app.route('/photo')
def f3():
    return render_template("photo.html")

@app.route('/time.html')
@app.route('/time/')
@app.route('/time')
def f4():
    return render_template("time.html")

@app.route('/gbook.html')
@app.route('/gbook/')
@app.route('/gbook')
def f5():
    return render_template("gbook.html")

@app.route('/about.html')
@app.route('/about/')
@app.route('/about')
def f6():
    return render_template("about.html")

@app.route('/release.html')
@app.route('/release/')
@app.route('/release')
def f7():
    return render_template("release.html")

@app.route('/login.html',methods=["GET","POST"])
@app.route('/login/',methods=["GET","POST"])
@app.route('/login',methods=["GET","POST"])
def f8():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        uname = request.form.get("username")
        upwd = request.form.get('password')
        s1 = sha1()
        s1.update(upwd.encode())
        upwd = s1.hexdigest()
        return '<h1>uname:%s,upwd:%s</h1>'%(uname,upwd)

@app.route('/register.html',methods=["GET",'POST'])
@app.route('/register/',methods=["GET",'POST'])
@app.route('/register',methods=["GET",'POST'])
def f9():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        uname = request.form.get('username')
        email = request.form.get('email')
        url = request.form.get('url')
        # upwd = request.form.get('password')
        # s1 = sha1()
        # s1.update(upwd.encode())
        # upwd = s1.hexdigest()
        upwd = generate_password_hash(request.form["password"])
        pwd = check_password_hash(upwd,request.form["password"])
        print(pwd)
        return '<h2>用户名:%s<br>邮箱:%s<br>主页地址:%s<br>密码:%s</h2>'%(uname,email,url,upwd)





if __name__ == "__main__":
    app.run(debug=True)
    # manager.run()
