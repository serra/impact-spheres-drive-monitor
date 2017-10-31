import os
from slackclient import SlackClient

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
MARIJN_IM_ID = 'D5RBMJ8RF'
IMPACT_SPHERES_ID = 'G7B5DUUC8'

DEFAULT_MSG = 'Hello from Python! :tada:'


sc = SlackClient(SLACK_BOT_TOKEN)


def send_message_to(channel,
                    message=DEFAULT_MSG):
    sc.api_call(
        "chat.postMessage",
        channel=channel,
        text=message
    )


def main():
    send_message_to(MARIJN_IM_ID)


if __name__ == '__main__':
    main()
