from flask import Flask, request
from google import guide_reports

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return 'This is the Impact Spheres Slack app.'


@app.route("/guides", methods=["POST"])
def guides():
    return "We will return guide info here ..."
