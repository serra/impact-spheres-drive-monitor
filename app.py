from flask import Flask, request
from google.guide_reports import markdown_report
from decorators import async
import requests

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return 'This is the Impact Spheres Slack app.'


@app.route("/guides", methods=["POST"])
def guides():
    # to do: verify Slack token
    post_report(request.form['response_url'])
    return "Working on those reports ... you'll hear from me soon!"


@app.route("/echo", methods=["POST"])
def echo():
    print(request)
    print(request.data)
    return 'echo'

# Delayed reponses


@async
def post_report(response_url):
    report = 'this will be the \n markdown-ish formatted report'  # markdown_report()
    print('posting report to <{0}>'.format(response_url))
    requests.post(response_url, data=report.encode(encoding='utf-8'))
    pass
