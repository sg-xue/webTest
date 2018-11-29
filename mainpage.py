#!/usr/bin/env python
# coding=utf8

from flask import Flask, request, render_template
import getSMS


app = Flask('webtest')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/search/', methods=['GET'])
def search():
    if request.args.get('phone_num'):
        search_tel = request.args.get('phone_num')
        # search_tel = search_tel.replace(' ', '')
        ShortMsg = getSMS.getMsg(search_tel)
        return render_template("search.html", ShortMsg=ShortMsg)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.debug = app.config.from_pyfile('./conf/config.py', silent=True)
    app.run()
