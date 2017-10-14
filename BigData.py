# 添加注释
#coding=utf-8
#zhanxiaodingxiugai
from flask import Flask, render_template
from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/123')
def hello1():
    return render_template("calendar.html")


@app.route('/1234')
def hello2():
    return render_template("chartjs.html")


@app.route("/bigData")
def big():
    return "bigData"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888)
