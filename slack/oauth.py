import os
from flask import Flask, request
from slackclient import SlackClient

client_id = os.environ["SLACK_CLIENT_ID"]
client_secret = os.environ["SLACK_CLIENT_SECRET"]
oauth_scope = os.environ["SLACK_BOT_SCOPE"]

app = Flask(__name__)


@app.route("/begin_auth", methods=["GET"])
def pre_install():
    return '''
      <a href="https://slack.com/oauth/authorize?scope={0}&client_id={1}&redirect_uri={2}">
          Add to Slack
      </a>
    '''.format(oauth_scope, client_id, 'http://localhost:5000/finish_auth')


@app.route("/finish_auth", methods=["GET", "POST"])
def post_install():

    # Retrieve the auth code from the request params
    auth_code = request.args['code']

    # An empty string is a valid token for this request
    sc = SlackClient("")

    # Request the auth tokens from Slack
    auth_response = sc.api_call(
        "oauth.access",
        client_id=client_id,
        client_secret=client_secret,
        code=auth_code
    )

    access_token = auth_response['access_token']
    # Save the bot token to an environmental variable or to your data store
    # for later use
    print('''Access token:

     {0}

     '''.format(access_token))
    # print('SLACK_BOT_TOKEN: {0}'.format(
    #     auth_response['bot']['bot_access_token']))

    # Don't forget to let the user know that auth has succeeded!
    return 'Auth complete!<br />Your access token: {0}'.format(access_token)
