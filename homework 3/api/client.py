from datetime import datetime
from urllib.parse import urljoin
import requests


class UnexpectedResponseStatusException(Exception):
    pass


class UnobtainableCSRFTokenException(Exception):
    pass


class ApiClient:
    def __init__(self, config):
        self.credentials = config
        self.session = requests.Session()
        self.url_base = 'https://target.my.com/'
        self.csrftoken = None

    def _request(self, method, location, headers=None, data=None, expected_status=200, jsonify=True):
        if location.startswith('/'):
            url = urljoin(self.url_base, location)
        else:
            url = location

        response = self.session.request(method, url, headers=headers, data=data)

        if response.status_code != expected_status:
            raise UnexpectedResponseStatusException(f'got {response.status_code} {response.reason} for url "{url}"\n'
                                                    f'expected status code: {expected_status}')

        if jsonify:
            response = response.json()

        return response

    def _get_cookie_headers(self, cookies):
        headers = {
            'Cookie': ''
        }

        for i in range(len(cookies)):
            headers['Cookie'] += f'{cookies[i]}='

            if cookies[i] == 'csrftoken':
                headers['Cookie'] += f'{self.csrftoken}'
                headers['X-CSRFToken'] = f'{self.csrftoken}'
            else:
                headers['Cookie'] += f'{self.session.cookies.get(cookies[i])}'

            if i < len(cookies) - 1:
                headers['Cookie'] += '; '

        return headers

    def collect_csrftoken(self):
        location = '/csrf/'
        cookie_header = self._request(method='GET', location=location, jsonify=False).headers['set-cookie'].split(';')
        unformatted_token = [header for header in cookie_header if 'csrftoken' in header]

        if not unformatted_token:
            raise UnobtainableCSRFTokenException('unable to obtain csrf token')

        self.csrftoken = unformatted_token[0].split('=')[-1]

    def post_auth(self):
        url = 'https://auth-ac.my.com/auth'

        data = {
            'email': self.credentials['login'],
            'password': self.credentials['password'],
            'continue': urljoin(self.url_base, '/auth/mycom'),
            'failure': 'https://account.my.com/login'
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': self.url_base
        }

        response = self._request(method='POST', location=url, headers=headers, data=data, jsonify=False)
        assert self.url_base in response.url, 'login failed'

    def post_segment_create(self):
        location = '/api/v2/remarketing/segments.json?fields=id'

        data = '{"name":"' + str(datetime.now()) + '","pass_condition":1,"relations":[{' \
                                                   '"object_type":"remarketing_player",' \
                                                   '"params":{"type":"positive","left":365,"right":0}}]}'

        headers = self._get_cookie_headers(['csrftoken', 'mc', 'sdcs'])
        response = self._request(method='POST', location=location, data=data, headers=headers)
        return response['id']

    def get_segment_check(self, action, id_segment):
        location = '/api/v2/remarketing/segments.json?fields=id&limit=500'
        headers = self._get_cookie_headers(['mc', 'sdcs', 'mrcu'])
        response = self._request(method='GET', location=location, headers=headers)

        segment = [item for item in response['items'] if item['id'] == id_segment]

        if action == 'create':
            assert segment, 'unable to find the new segment'
        elif action == 'delete':
            assert not segment, 'failed to delete the segment'
        else:
            raise ValueError('"action" must be either "create" or "delete"')

    def delete_segment(self, id_segment):
        location = f'/api/v2/remarketing/segments/{id_segment}.json'
        headers = self._get_cookie_headers(['csrftoken', 'mc', 'sdcs', 'mrcu'])
        self._request(method='DELETE', location=location, headers=headers, expected_status=204, jsonify=False)

    def post_campaign_create(self):
        location = '/api/v2/campaigns.json'
        data = '{"name":"' + str(datetime.now()) + '","objective":"traffic","package_id":961,' \
                                                   '"banners":[{"urls":{"primary":{"id":47187547}},' \
                                                   '"content":{"image_240x400":{"id":8680529}}}]}'
        headers = self._get_cookie_headers(['csrftoken', 'mc', 'sdcs', 'mrcu'])
        return self._request(method='POST', location=location, headers=headers, data=data)['id']

    def post_campaign_delete(self, id_campaign):
        location = f'/api/v2/campaigns/{id_campaign}.json'
        data = '{"status":"deleted"}'
        headers = self._get_cookie_headers(['csrftoken', 'mc', 'sdcs', 'mrcu'])
        self._request(method='POST', location=location, data=data, headers=headers, expected_status=204, jsonify=False)

    def get_campaign_create_check(self, id_campaign):
        location = '/api/v2/campaigns.json?fields=id&limit=250&_status__in=active'
        headers = self._get_cookie_headers(['mc', 'sdcs', 'mrcu'])
        response = self._request(method='GET', location=location, headers=headers)

        created_campaign = [item for item in response['items'] if item['id'] == id_campaign]
        assert created_campaign, 'unable to find the new campaign'

        self.post_campaign_delete(id_campaign)  # автоматическое удаление
