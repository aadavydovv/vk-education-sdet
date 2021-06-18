from misc.constants import METHOD_GET, METHOD_POST, MYAPP_PORT
from urllib.parse import urljoin
import allure
import json
import requests


class APIClient:

    def __init__(self, logger):
        self.session = requests.Session()
        self.url_base = f'http://myapp:{MYAPP_PORT}/'
        self.logger = logger

    # main methods

    @allure.step('make the add user request with username {username}, password {password}, email {email}')
    def post_add_user(self, username, password, email):
        location = f'/api/add_user'

        headers = {
            'Content-Type': 'application/json'
        }

        if not (username or password or email):
            body = None
        else:
            body = json.dumps({
                'username': username,
                'password': password,
                'email': email
            })

        response = self._request(METHOD_POST, location, headers=headers, data=body)
        return response

    @allure.step('make the delete user request with username {username}')
    def get_delete_user(self, username):
        location = f'/api/del_user/{username}'

        response = self._request(METHOD_GET, location)
        return response

    @allure.step('make the block user request with username {username}')
    def get_block_user(self, username):
        location = f'/api/block_user/{username}'

        response = self._request(METHOD_GET, location)
        return response

    @allure.step('make the accept user request with username {username}')
    def get_accept_user(self, username):
        location = f'/api/accept_user/{username}'

        response = self._request(METHOD_GET, location)
        return response

    @allure.step('make the get app status request')
    def get_status(self):
        location = f'/status'

        response = self._request(METHOD_GET, location)
        return response

    # auxiliary methods

    def _request(self, method, location, headers=None, data=None):
        self.logger.info(f'sending a request: '
                         f'method - "{method}", '
                         f'location - "{location}", '
                         f'headers - {"empty" if (headers is None) else headers}, '
                         f'data - {"empty" if (data is None) else data}')

        url = urljoin(self.url_base, location)
        response = self.session.request(method, url, headers=headers, data=data)

        if response.headers.get('Content-Type') == 'application/json':
            response_body = response.json()
        else:
            response_body = '...'

        self.logger.info(f'got a response: '
                         f'status - {response.status_code}, '
                         f'headers - {response.headers if response.headers else "empty"}, '
                         f'body - {response_body}')
        return response

    @allure.step('make the register user request with username {username}, password {password}, email {email}')
    def post_register_user(self, username, password, email):
        location = '/reg'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'username': username,
            'email': email,
            'password': password,
            'confirm': password,
            'term': 'y',
            'submit': 'Register'
        }

        self._request(METHOD_POST, location, headers=headers, data=body)

    @allure.step('make the authorize user request with username {username}, password {password}')
    def post_authorize(self, username, password):
        location = '/login'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'username': username,
            'password': password,
            'submit': 'Login'
        }

        self._request(METHOD_POST, location, headers=headers, data=body)
