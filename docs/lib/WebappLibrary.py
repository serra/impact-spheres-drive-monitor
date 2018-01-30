import requests


class WebappLibrary:

    def __init__(self):
        self._host = 'http://localhost:5000'

    def slack_can_request_guide_reports(self):
        url = '{0}/guides'.format(self._host)
        data = {
            'response_url': 'http://localhost:5000/echo',
            'text': '',
        }
        r = requests.post(url, data=data)
        r.raise_for_status()

    def the_addon_can_search_guides(self):
        url = '{0}/search'.format(self._host)
        data = {
            'query': 'wall',
        }
        r = requests.get(url, data=data)
        r.raise_for_status()
