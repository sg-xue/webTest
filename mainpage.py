#!/usr/bin/env python
# coding=utf8

from flask import Flask, request, render_template
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
import getSMS


class MyForm(Form):
    user = StringField("Username", validators=[DataRequired()])

app = Flask(__name__)
# app.config.from_pyfile('../conf/config.py', silent=True)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/search/', methods=['GET'])
def search():
    if request.args.get('phone_num'):
        search_tel = request.args.get('phone_num')
        return render_template("search.html", ShortMsg=getSMS.getMsg(search_tel))
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.debug = app.config.from_pyfile('./conf/config.py')
    app.run()
