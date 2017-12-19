from contentful_management import Client
import os
import requests

ACCESS_TOKEN = os.environ['CONTENTFUL_TOKEN']
GUIDES_SPACE_ID = 'eqk5645yz1a7'
API_URL = 'api.contentful.com'

def get_client():
    client = Client(ACCESS_TOKEN,
                    api_url=API_URL)
    return client


def get_guides_space():
    client = get_client()
    return client.spaces().find(GUIDES_SPACE_ID)


def get_guides_content_type():
    return get_guides_space().content_types().find('guide')


def search_guides(query):
    #result = get_guides_content_type().entries({'query': query, 'content_type': 'guide'})

    url = f'https://{API_URL}/spaces/{GUIDES_SPACE_ID}/entries?' \
          f'access_token={ACCESS_TOKEN}' \
          f'&content_type=guide&query={query}' \
          f'&select=sys.id,fields.title,fields.description'

    r = requests.get(url)
    data = r.json()

    for item in data['items']:
        yield {'id': item['sys']['id'], 'title': item['fields']['title']['en-US']}


def find_guide(guide_id):
    get_guides_space().entries().find(guide_id)

