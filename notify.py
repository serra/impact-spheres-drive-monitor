from google.guide_reports import to_review
from slack.post import send_message_to
import os


def main():
    channel = os.environ["SLACK_CHANNEL_TO_NOTIFY"]

    print('Retrieving report ... ')
    msg = to_review()
    print(msg)
    print('Sending report to agilityscales.slack.com ... ')
    send_message_to(channel, msg)
    print('Done.')


if __name__ == '__main__':
    main()
