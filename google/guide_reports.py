# -*- coding: utf-8 -*-
from .oauth import get_service
from io import BytesIO
from googleapiclient.http import MediaIoBaseDownload
from re import compile as compile_regex

# Impact Spheres constants
PRACTICES_AND_GUIDES_FOLDER_ID = '0B-_LfsRTnsW8N1lOZ0dDUTYwWUE'
# for testing purposes
A_PUBLIC_FOLDER_ID = '0B6jUQ8RVhYDgN0xNaEZON0Z3TFE'
A_PRIVATE_FOLDER_ID = '0B6jUQ8RVhYDgdFZ5RXMtYVQ4V28'

_count_ok_regex = compile_regex(":\s*[Oo][Kk]")


def iterate_guides(service, folder_id):
    page_token = None
    while True:
        results = service.files().list(q="'" + folder_id + "' in parents" +
                                         " and mimeType = 'application/vnd.google-apps.document'",
                                       orderBy='name',
                                       pageSize=10,
                                       fields='nextPageToken, files(id, name, modifiedTime, version)',
                                       pageToken=page_token).execute()
        files = results.get('files', [])
        for file in files:
            yield (file)
        page_token = results.get('nextPageToken', None)
        if page_token is None:
            break


def count_guides(service, folder_id):
    files = []

    for file in iterate_guides(service, folder_id):
        files.append(file)

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


def get_review_folder(folders):
    return next(f for f in folders if f['name'] == '3-In Review')


def get_folders_with_file_counts(service):
    folders = sorted(get_process_folders(service),
                     key=lambda f: f['name'])

    if not folders:
        print('No files found.')
    else:
        for f in folders:
            f['file_count'] = count_guides(service, f['id'])
    return folders


def get_report_line(folder):
    n = folder['file_count']
    max_bar = 20
    bar = '-' * min(n, max_bar)
    if n > max_bar:
        bar = bar + ' 💥 '
    if n == 0:
        bar = '👏'
    line = ' {0:<15} {1:>3} {2}'.format(folder['name'], n, bar)
    return line


def report_queues(folders):
    s = 'Guides: '
    for f in folders:
        s = '{0}\n{1}'.format(s, get_report_line(f))
    return s


def report_files_to_review(folders, service):
    f = get_review_folder(folders)
    shortened_review_url = 'https://goo.gl/pib2RV'
    guides = []

    for file in iterate_guides(service, f['id']):
        file['ok_count'] = count_oks(service, file['id'])
        guides.append(file)

    s = 'Guides to review:'
    for g in guides:
        s = '{0}\n  {1}x👍  {2}'.format(s, g['ok_count'], g['name'])

    s = '{0} \n\nReview folder: {1}'.format(s, shortened_review_url)
    return s


def count_oks(service, file_id):
    request = service.files().export_media(fileId=file_id,
                                           mimeType='text/plain')
    fh = BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    b = fh.getvalue()
    s = b.decode('UTF-8')
    return count_oks_in(s)


def count_oks_in(s):
    return len(_count_ok_regex.findall(s))


def queues():
    service = get_service(use_oauth=True)
    folders = get_folders_with_file_counts(service)
    return '```{0}```'.format(report_queues(folders))


def to_review():
    service = get_service(use_oauth=True)
    folders = get_folders_with_file_counts(service)
    return report_files_to_review(folders, service)


def markdown_report():
    service = get_service(use_oauth=True)
    folders = get_folders_with_file_counts(service)
    qs = report_queues(folders)
    rv = report_files_to_review(folders, service)

    rep = '{0} \n\n ```\n{1}\n``` \n'.format(rv, qs)
    return rep


report_map = {'queues': queues,
              'review': to_review,
              'daily': markdown_report}


def get_report(report_key='queues'):
    key = report_key
    if key not in report_map:
        key = 'queues'
    return report_map[key]()


def print_report():
    print(markdown_report())


def main():
    print_report()
