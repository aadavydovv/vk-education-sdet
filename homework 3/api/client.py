from datetime import datetime
from urllib.parse import urljoin
import requests


class UnexpectedResponseStatusException(Exception):
    pass


class UnobtainableCSRFTokenException(Exception):
    pass


class ApiClient:
    def __init__(self, config):
        self.cookies = {}
        self.credentials = config
        self.session = requests.Session()
        self.url_base = 'https://target.my.com/'

        self.id_new_campaign = None
        self.id_new_segment = None

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

    def _collect_csrftoken(self):
        location = '/csrf/'
        cookie_header = self._request(method='GET', location=location, jsonify=False).headers['set-cookie'].split(';')
        unformatted_token = [header for header in cookie_header if 'csrftoken' in header]

        if not unformatted_token:
            raise UnobtainableCSRFTokenException('unable to obtain csrf token')

        self.cookies['csrftoken'] = unformatted_token[0].split('=')[-1]

    def _get_cookie_headers(self, cookies):
        headers = {
            'Cookie': ''
        }

        for cookie in cookies:
            headers['Cookie'] += f'{cookie}={self.cookies[cookie]}; '

            if cookie == 'csrftoken':
                headers['X-CSRFToken'] = f'{self.cookies[cookie]}'

        headers['Cookie'] = headers['Cookie'][:-2]

        return headers

    def collect_cookies(self):
        self.cookies['mc'] = self.session.cookies.get('mc')
        self.cookies['mrcu'] = self.session.cookies.get('mrcu')
        self.cookies['sdcs'] = self.session.cookies.get('sdcs')

        self._collect_csrftoken()

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
        self.id_new_segment = response['id']

    def get_segment_check(self, action):
        location = '/api/v2/remarketing/segments.json?fields=id&limit=500'
        headers = self._get_cookie_headers(['mc', 'sdcs', 'mrcu'])
        response = self._request(method='GET', location=location, headers=headers)

        segment = [item for item in response['items'] if item['id'] == self.id_new_segment]

        if action == 'create':
            assert segment, 'unable to find the new segment'
        elif action == 'delete':
            assert not segment, 'failed to delete the segment'
        else:
            raise ValueError('"action" must be either "create" or "delete"')

    def post_segment_delete(self):
        location = '/api/v1/remarketing/mass_action/delete.json'
        data = '[{"source_id":' + str(self.id_new_segment) + ',"source_type":"segment"}]'
        headers = self._get_cookie_headers(['csrftoken', 'mc', 'sdcs', 'mrcu'])
        self._request(method='POST', location=location, data=data, headers=headers)

    def post_campaign_create(self):
        location = '/api/v2/campaigns.json'
        data = '{"name":"' + str(datetime.now()) + '","objective":"traffic","package_id":961,' \
                                                   '"banners":[{"urls":{"primary":{"id":47187547}},' \
                                                   '"content":{"image_240x400":{"id":8680529}}}]}'
        headers = self._get_cookie_headers(['csrftoken', 'mc', 'sdcs', 'mrcu'])
        self.id_new_campaign = self._request(method='POST', location=location, headers=headers, data=data)['id']

    def post_campaign_delete(self):
        location = f'/api/v2/campaigns/{self.id_new_campaign}.json'
        data = '{"status":"deleted"}'
        headers = self._get_cookie_headers(['csrftoken', 'mc', 'sdcs', 'mrcu'])
        self._request(method='POST', location=location, data=data, headers=headers, expected_status=204, jsonify=False)

    def get_campaign_create_check(self):
        location = '/api/v2/campaigns.json?fields=id&limit=250&_status__in=active'
        headers = self._get_cookie_headers(['mc', 'sdcs', 'mrcu'])
        response = self._request(method='GET', location=location, headers=headers)

        created_campaign = [item for item in response['items'] if item['id'] == self.id_new_campaign]
        assert created_campaign, 'unable to find the new campaign'

        self.post_campaign_delete()  # автоматическое удаление
