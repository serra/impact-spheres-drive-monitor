# Impact Spheres Drive Monitor

Scripts to monitor the Impact Sphere practices and guides folder to monitor flow and support writing guides.

Ask [Marijn on Slack] if you want to contribute.

## Installing

For use in Slack: see usage.

For use in Google Docs: install the add-on. A link to the add-on is distributed through Slack.

## Usage 

Just use Slack. At regular intervals the bot will notify the `#09_impactspheres` channel of guide statuses.

You can also use the `/guides` Slash Command:


---


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
