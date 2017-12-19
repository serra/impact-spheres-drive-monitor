from flask import Flask, request, jsonify
from google.guide_reports import get_report
from content.guides import search_guides
from decorators import async
import requests


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return 'This is the Impact Spheres Slack app.'


@app.route("/guides", methods=["POST"])
def guides():
    text = request.form['text']
    key = text.split(' ', 1)[0]
    post_report(request.form['response_url'], key)
    return "Working on those reports ... you'll hear from me soon!"


@app.route("/search", methods=["GET"])
def search():
    text = request.args.get('query')
    guides = search_guides(text)
    return jsonify(list(guides))


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
