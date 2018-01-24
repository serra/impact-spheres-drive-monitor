# Impact Spheres Drive Monitor

Scripts to monitor the Impact Sphere practices and guides folder to monitor flow and support writing guides.

Ask [Marijn on Slack] if you want to contribute.

## Installing

For use in Slack: see usage.

For use in Google Docs: install the add-on. A link to the add-on is distributed through Slack.

## Usage 

Just use Slack. At regular intervals the bot will notify the `#09_impactspheres` channel of guide statuses.

You can also use the `/guides` Slash Command:


### App management

The app requires access to agilityscales.slack.com.
It gets this access as the [Impact Spheres App] there.

The app requires access to the Impact Spheres folder on Gooogle Drive.
It uses the impactspheres@gmail.com credentials to access this folder.

The app runs on Heroku, under Marijn's Heroku account.

### Security

Be careful with using your credentials to authorize the app to do work on your behalf.

#### Google Drive & security



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

Open a browser at http://localhost:5000/begin_auth.
Follow the link to start an oauth flow.
A token will be created on your behalf.

#### Contentful

Guides are stored in a Contentful document store.
It has an API that uses OAuth2 for authentication.
This application was created by follwing the section 
"Creating an OAuth 2.0 application" in [Contentful docs on authentication].

Client id and secret are managed from Marijn's Contentful account.

You can authorize your script for local development:

```
make auth-contentful
```

Open a browser at http://localhost:5000/begin_auth.
Follow the link to start an oauth flow.
A token will be created on your behalf.


### Run tests

Running

```
make test
```

Connects to Google drive and prints the guides overview.

In addition, some Python unit tests are available in `./tests/`.

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
 [Slash Commands]: https://api.slack.com/slash-commands
 [Contentful docs on authentication]: https://www.contentful.com/developers/docs/references/authentication/
