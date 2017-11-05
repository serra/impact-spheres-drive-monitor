# Impact Spheres Drive Monitor

Script to monitor the Impact Sphere practices and guides folder to monitor flow.

Ask [Marijn on Slack] if you want to contribute.

## Installing

```
todo
```

## Usage

```
todo
```

## Developing

Developed on OSX, Python version 3.6.

### Prepare environment

Assuming virtualenv 1.7+:

```
cd [impact-spheres-drive-monitor]
virtualenv -p /usr/local/bin/python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

### Developing & hacking

```
. venv/bin/activate
python monitor.py
```


### App management

The app requires access to agilityscales.slack.com.
It gets this access as the [Impact Spheres App] there.

The app requires access to the Impact Spheres folder on Gooogle Drive.
It uses the impactspheres@gmail.com credentials to access this folder.

The app runs on Heroku, under Marijn's Heroku account.

### Security

Be careful with using your credentials to authorize the app to do work on your behalf.

#### Google Drive & security

To use this script you'll need a Google account.

To access public drive files, you only need a Google API key. 
You can configure access using the [Google API management console].

To access private drive files, an authorized human being has to give consent.
This consent can be given using OAuth2. 
BEWARE, giving consent gives the script access to ALL your data on Google Drive,
From the moment you give consent, the script can impersonate you
as long as the client ID is active.
That's why I gve consent using the impactspheres@gmail.com Google account.

See the [Drive Python API quickstart] for information on using OAuth
in the context of Google drive.

Do NOT share your OAuth client secret. 
To avoid accidental sharing of client secrets, I have added it to .gitignore.

API keys as well as client IDs can be managed in your personal
[Google API management console].

#### Slack and security

Slack uses OAuth2 as well. 
The [Slack sign-in process] is documented well; worth a quick read.
As with Google authorization, be careful with your login credentials,
as those allow others to post to Slack on your behalf.

Currently the Slack client id and secret are managed from Marijn's Slack account.

You can authorize your script for local development:

```
make auth-slack
```

Open a browser at http://localhost/begin_auth.
Follow the link to start an oauth flow.
A token will be created on your behalf.


### Run tests

None available yet.

Running

```
make test
```

Connects to Google drive and prints the guides overview.

### Packaging & Publishing

Not available as a package yet.

### Continuous Integration

Not available yet.

## References

 [Drive Python API quickstart]: https://developers.google.com/drive/v3/web/quickstart/python
 [Python Drive API]: https://developers.google.com/resources/api-libraries/documentation/drive/v3/python/latest/
 [Google API management console]: https://console.developers.google.com/apis/credentials?project=ageless-aquifer-176113
 [Slack Python API]: http://slackapi.github.io/python-slackclient/basic_usage.html#sending-a-message
 [Slack sign-in process]: https://api.slack.com/docs/sign-in-with-slack
 [Impact Spheres App]: https://agilityscales.slack.com/apps/A7RHUFQ90-impact-spheres-app
 [Marijn on Slack]: https://agilityscales.slack.com/messages/C3N27KRT9/team/U5S1Q0YQ5/

