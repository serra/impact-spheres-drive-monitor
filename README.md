# Impact Spheres Drive Monitor

Script to monitor the Impact Sphere practices and guides folder to monitor flow.


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

To use this script you'll need a Google account.

To access public drive files, you only need a Google API key. 
See references to create such a key.

To access private drive files, an authorized human being has to give consent.
This consent can be given using OAuth2. 
BEWARE, giving consent gives the script access to ALL your data on Google Drive,
From the moment you give consent, the script can impersonate you
as long as the client ID is active.

See the [Drive Python API quickstart] for information on using OAuth
in the context of Google drive.

Do NOT share your OAuth client secret. 
To avoid accidental sharing of client secrets, I have added it to .gitignore.

API keys as well as client IDs can be managed in your personal
[Google API management console].

### Run tests

None available yet.

### Packaging & Publishing

Not available as a package yet.

### Continuous Integration

Not available yet.

## References

 [Drive Python API quickstart]: https://developers.google.com/drive/v3/web/quickstart/python
 [Python Drive API]: https://developers.google.com/resources/api-libraries/documentation/drive/v3/python/latest/
 [Google API management console]: https://console.developers.google.com/apis/credentials?project=ageless-aquifer-176113

