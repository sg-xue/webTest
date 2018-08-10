#!/usr/bin/env python
# coding=utf8

from flask import Flask, request, render_template
import getSMS


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/search/', methods=['GET'])
def search():

    if request.args.get('phone_num'):
        search_tel = request.args.get('phone_num')
        search_tel = search_tel.replace(' ', '')
        return render_template("search.html", ShortMsg=getSMS.getMsg(search_tel))
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.debug = app.config.from_pyfile('./conf/config.py', silent=True)
    app.run()
