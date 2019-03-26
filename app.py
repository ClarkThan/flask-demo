# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
db = SQLAlchemy()
db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/no')
def index_no():
    return '这里没有使用模板文件, 直接返回<h2>字符串</h2>给前端浏览器'


@app.route('/tb')
def table():
    result = '<table border="1">'

    ds = db.session.query(User.name, User.email).limit(5).all()
    for u in ds:
        row = '<tr><td>{}</td><td>{}</td></tr>'.format(u.name, u.email)
        result += row

    result += '</table>'
    return result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', your_name=name)


if __name__ == '__main__':
    app.run()
