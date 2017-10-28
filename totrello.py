import monitor
import os
from trello import TrelloClient


def get_client():
    api_key = os.environ["TRELLO_API_KEY"]
    client = TrelloClient(api_key=api_key)
    return client


def get_board(api):
    board = api.get_board('pOpy8cnB')
    return board


def add_card(description, list):
    pass


def list_cards(list_name):
    pass


def move_card(file, folder):
    print(' {0} ({1}..) >> {2}'.format(
        file['name'], file['id'][:5], folder['name']))


def sync_folder(service, folder, board):
    current_folder = folder['name']
    list_cards(current_folder)

    lsts = [lst for lst in board.list_lists() if lst.name == current_folder]

    if len(lsts) < 1:
        print('Stopping sync. No matching Trello list found for {0}'.format(
            current_folder))
        return

    def callback(file):
        move_card(file, folder)

    monitor.iterate_files(service, folder['id'], callback)


def main():
    drive_service = monitor.get_service(use_oauth=True)
    folders = monitor.get_process_folders(drive_service)
    board = get_board(get_client())

    if not folders:
        print('No folders found.')
    else:
        print('Folders:')
        for folder in folders:
            sync_folder(drive_service, folder, board)


if __name__ == '__main__':
    main()
