# coding=utf-8

from flask import Flask, render_template
import config
from exts import db
from models import *
import time
import json

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/safe")
def safe():
    last_month = time.localtime(time.time() - 30 * 24 * 3600)
    datas = SafeProblem.query.filter(SafeProblem.D_CHECKDATE >= last_month)
    return render_template("safe.html", datas=datas)


@app.route("/safe/json")
def safe_json():
    last_month = time.localtime(time.time() - 30 * 24 * 3600)
    datas = SafeNumber.query.filter(SafeNumber.TIME > last_month)
    json_data = {
        "column": [],
        "data": []
    }
    for data in datas:
        json_data["column"].append(data.DEPT_NAME)
        json_data["data"].append(data.NUMBER)

    return json.dumps(json_data)


if __name__ == '__main__':
    app.run(debug=True, port=8888)
