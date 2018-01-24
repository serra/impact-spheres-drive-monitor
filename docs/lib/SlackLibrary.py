from context import slack
from slack import post

MARIJN_DM_ID = 'D5RBMJ8RF'


class SlackLibrary:

    def __init__(self):
        pass

    def send_marijn_a_direct_message(self):
        post.send_message_to(MARIJN_DM_ID,
                             'I am setting up my development environment'
                             'to work on the Impact Spheres Scripts.')
