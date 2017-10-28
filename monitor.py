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
# for testing purposes
A_PUBLIC_FOLDER_ID = '0B6jUQ8RVhYDgN0xNaEZON0Z3TFE'
A_PRIVATE_FOLDER_ID = '0B6jUQ8RVhYDgdFZ5RXMtYVQ4V28'


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


def iterate_files(service, folder_id, callback):
    page_token = None
    while True:
        results = service.files().list(q="'" + folder_id + "' in parents",
                                       orderBy='name',
                                       pageSize=10,
                                       fields='nextPageToken, files(id, name)',
                                       pageToken=page_token).execute()
        files = results.get('files', [])
        for file in files:
            callback(file)
        page_token = results.get('nextPageToken', None)
        if page_token is None:
            break


def count_files(service, folder_id):
    files = []

    def callback(file):
        files.append(file)

    iterate_files(service, folder_id, callback)

    return len(files)


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


def get_service(use_oauth=False):
    http = None
    if use_oauth:
        credentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('drive', 'v3', http=http)
    api_key = os.environ["GOOGLE_API_KEY"]
    service = discovery.build('drive', 'v3', http=http, developerKey=api_key)
    return service


def get_folders_with_file_counts(service):
    folders = sorted(get_process_folders(service),
                     key=lambda f: f['name'])

    if not folders:
        print('No files found.')
    else:
        for f in folders:
            f['file_count'] = count_files(service, f['id'])
    return folders


def report_queues(folders):
    s = 'Guides: '
    for f in folders:
        n = f['file_count']
        bar = '-' * min(n, 20)
        if(n > 20):
            bar = bar + ' + '
        s = '{3}\n{0:<15} {1:>3} {2}'.format(f['name'], n, bar, s)
    return s


def main():
    service = get_service(use_oauth=True)
    folders = get_folders_with_file_counts(service)
    print(report_queues(folders))


if __name__ == '__main__':
    main()
