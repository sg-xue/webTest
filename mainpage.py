#!/usr/bin/env python
# coding=utf8

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


app = Flask(__name__)
app.config.from_pyfile('../conf/main_config.py', silent=True)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run()
