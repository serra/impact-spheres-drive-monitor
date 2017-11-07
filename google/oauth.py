from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client.client import Credentials
from oauth2client import tools
from oauth2client.file import Storage

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/impact-spheres-drive-monitor.json
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'drive_client_secret.json'
APPLICATION_NAME = 'Impact Spheres Drive Monitor'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    if use_credentials_from_environment():
        print('Using Google credentials from environment ... ')
        return get_credentials_from_environment()

    print('Using Google credentials from storage ... ')
    return get_credentials_from_storage()


def get_credentials_path():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    return os.path.join(credential_dir, 'impact-spheres-drive-monitor.json')


def get_credentials_from_storage():
    credential_path = get_credentials_path()

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flags = None
        try:
            import argparse
            flags = argparse.ArgumentParser(
                parents=[tools.argparser]).parse_args()
        except ImportError:
            flags = None
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def use_credentials_from_environment():
    return ('GOOGLE_CREDENTIALS' in os.environ)


def get_credentials_from_environment():
    json_data = os.environ['GOOGLE_CREDENTIALS']
    return Credentials.new_from_json(json_data)


def get_service(use_oauth=False):
    http = None
    if use_oauth:
        credentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('drive', 'v3', http=http)
    api_key = os.environ["GOOGLE_API_KEY"]
    service = discovery.build('drive', 'v3', http=http, developerKey=api_key)
    return service


def main():
    credentials = get_credentials_from_storage()
    print('Found credentials in storage: {0}...'.format(
        credentials.to_json()[:25]))
    if(use_credentials_from_environment()):
        print('This environment uses credentials from environment variables.')

    print('''
        To setup new credentials, remove the file
        {0}.
        Then run this script again.
        '''.format(get_credentials_path()))

    print('''
        Use the following line to add the credentials to an env variable:

        export GOOGLE_CREDENTIALS="{0}"
        '''.format(credentials.to_json().replace('"', '\\"')))


if __name__ == '__main__':
    main()
