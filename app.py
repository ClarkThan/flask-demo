# -*- coding: utf-8 -*-
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/no')
def index_no():
    return '这里没有使用模板文件, 直接返回<h2>字符串</h2>给前端浏览器'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', your_name=name)



if __name__ == '__main__':
    app.run()