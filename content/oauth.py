import os
from flask import Flask, request

client_id = os.environ["CONTENTFUL_CLIENT_ID"]
oauth_scope = "content_management_read"

app = Flask(__name__)


@app.route("/begin_auth", methods=["GET"])
def pre_install():
    return '''
    <p>
    After authentication, you will be redirected to {2}.
    There you can get the access token from the query string.
    </p>
    <p>
      <a href="https://be.contentful.com/oauth/authorize?response_type=token&scope={0}&client_id={1}&redirect_uri={2}">
          Get a Contentful access token
      </a>
    </p>
    '''.format(oauth_scope, client_id, 'https://impact-spheres-drive-monitor.herokuapp.com')
