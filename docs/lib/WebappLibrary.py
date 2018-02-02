import requests


class WebappLibrary:

    def __init__(self):
        self._host = 'http://localhost:5000'

    def get_response(self, command, text):
        url = '{0}/{1}'.format(self._host, command)
        data = {
            'response_url': 'http://localhost:5000/echo',
            'text': text,
        }
        r = requests.post(url, data=data)
        return r

    def slack_can_request_guide_reports(self):
        self.valid_command('guides')

    def valid_command(self, command, text=''):
        r = self.get_response(command, text)
        r.raise_for_status()

    def invalid_command(self, command, text=''):
        r = self.get_response(command, text)
        assert r.status_code >= 400, '"/{0} {1}" should return an error, but instead got {2}'.format(
            command, text, r.status_code)

    def the_addon_can_search_guides(self):
        url = '{0}/search'.format(self._host)
        data = {
            'query': 'wall',
        }
        r = requests.get(url, data=data)
        r.raise_for_status()
