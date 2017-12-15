from contentful import Client
import os

ACCESS_TOKEN = os.environ['CONTENTFUL_TOKEN']
GUIDES_SPACE_ID = 'eqk5645yz1a7'


def get_client():
    client = Client(GUIDES_SPACE_ID,
                    ACCESS_TOKEN,
                    api_url='api.contentful.com',
                    default_locale='en-US')
    return client


def search_guides(query):
    result = get_client().entries({'query': query, 'content_type': 'guide'})
    for item in result.items:
        yield {'id': item.id, 'title': item.title}
