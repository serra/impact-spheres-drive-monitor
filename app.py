from flask import Flask, request
from google.guide_reports import markdown_report

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return 'This is the Impact Spheres Slack app.'


@app.route("/guides", methods=["POST"])
def guides():
    # to do: verify Slack token
    return markdown_report()
