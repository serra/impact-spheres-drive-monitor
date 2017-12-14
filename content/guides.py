from contentful import Client
import os

ACCESS_TOKEN = os.environ['CONTENTFUL_TOKEN']
GUIDES_SPACE_ID = 'eqk5645yz1a7'
BIG_WALL_GUIDE_ID = '1Cgku5owWkuaQAGo4oegOy'

def get_client():
    client = Client(GUIDES_SPACE_ID, ACCESS_TOKEN, api_url='api.contentful.com')
    return client