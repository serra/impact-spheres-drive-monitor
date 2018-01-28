# -*- coding: utf-8 -*-

import sys
import os
from flask import Flask, request, jsonify, render_template
import requests
from flask_bootstrap import Bootstrap

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from google.guide_reports import get_report
from content.guides import search_all
from decorators import async


def get_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app


app = get_app()


@app.route("/", methods=["GET"])
def index():
    volunteers = [
        {'name': 'Jurgen Appelo', 'id': '2JlqZjrezCwcSgAYu4Q4QU'},
        {'name': 'Eddy Bruin', 'id': '4vFByVjTOo8CCgakYU8KYS'},
        {'name': 'Hugo Emond', 'id': '1ZC1kuRG1emM62aQMgEOqa'},
        {'name': 'Jürgen Knuplesch', 'id': '2dO882sGPmIOOOyGaK0cQ4'},
        {'name': 'Dov Tsal', 'id': '3i9qaKwbJeWg80AUm28Aw6'},
        {'name': 'Marijn van der Zee', 'id': '5oGDjpcUNymKUuIqkko0aQ'},
        {'name': 'Frederik Vannieuwenhuyse', 'id': '3I4nO354qkKacukGKAKoWA'},
        {'name': 'John Williams', 'id': '1JrD9EhVeUM84ceaKu0Css'},
    ]
    return render_template('index.html', volunteers=volunteers)


@app.route("/guides", methods=["POST"])
def guides():
    text = request.form['text']
    key = text.split(' ', 1)[0]
    post_report(request.form['response_url'], key)
    return "Working on those reports ... you'll hear from me soon!"


@app.route("/search", methods=["GET"])
def search():
    text = request.args.get('query')
    items = search_all(text)
    return jsonify(list(items))


@app.route("/echo", methods=["POST"])
def echo():
    print(request)
    print(request.data)
    return 'echo'

# Delayed reponses


@async
def post_report(response_url, report_key):
    report = get_report(report_key)
    data = {'text': report}

    print('posting report to <{0}>'.format(response_url))
    requests.post(response_url, json=data)
    pass
