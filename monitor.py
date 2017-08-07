from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/impact-spheres-drive-monitor.json
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Impact Spheres Drive Monitor'


# Impact Spheres constants
PRACTICES_AND_GUIDES_FOLDER_ID = '0B-_LfsRTnsW8N1lOZ0dDUTYwWUE'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'impact-spheres-drive-monitor.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def count_files(service, folder_id):
    page_token = None
    file_count = 0
    while True:
        results = service.files().list(q="'" + folder_id + "' in parents",
                                       orderBy='name',
                                       pageSize=10,
                                       fields='nextPageToken, files(id, name)',
                                       pageToken=page_token).execute()
        files = results.get('files', [])
        file_count += len(files)
        page_token = results.get('nextPageToken', None)
        if page_token is None:
            break

    return file_count


def get_process_folders(service):
    query = "'" + PRACTICES_AND_GUIDES_FOLDER_ID + "' in parents " + \
        "and mimeType = 'application/vnd.google-apps.folder'"

    results = service.files().list(
        q=query,
        pageSize=10,
        orderBy='name',
        fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    return items


def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    items = get_process_folders(service)

    if not items:
        print('No files found.')
    else:
        print('Folders:')
        for item in items:
            item['file_count'] = count_files(service, item['id'])
            print('{0} ({1} files)'.format(item['name'], item['file_count']))


if __name__ == '__main__':
    main()
