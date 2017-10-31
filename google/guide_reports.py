from .oauth import get_service

# Impact Spheres constants
PRACTICES_AND_GUIDES_FOLDER_ID = '0B-_LfsRTnsW8N1lOZ0dDUTYwWUE'
# for testing purposes
A_PUBLIC_FOLDER_ID = '0B6jUQ8RVhYDgN0xNaEZON0Z3TFE'
A_PRIVATE_FOLDER_ID = '0B6jUQ8RVhYDgdFZ5RXMtYVQ4V28'


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
            yield(file)
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
    bar = '-' * min(n, 20)
    if(n > 20):
        bar = bar + ' + '
    if(n == 0):
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
    url = 'https://drive.google.com/drive/u/0/folders/{0}'.format(f['id'])
    guides = []

    for file in iterate_guides(service, f['id']):
        guides.append(file)

    s = 'Guides to review:'
    for g in guides:
        s = '{0}\n  {1}'.format(s, g['name'], url)

    s = '{0} \n\nreview folder: {1}'.format(s, url)
    return s


def print_report():
    service = get_service(use_oauth=True)
    folders = get_folders_with_file_counts(service)

    print('```')
    print(report_queues(folders))
    print('```')
    print()
    print(report_files_to_review(folders, service))


def main():
    print_report()


if __name__ == '__main__':
    main()
