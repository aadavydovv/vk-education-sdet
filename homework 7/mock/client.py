from mock.constants import *
import json
import socket


class HTTPClient:

    def _connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(0.1)
        self.client.connect((MOCK_HOST, int(MOCK_PORT)))

    def _receive(self):
        data = []

        while True:
            data_part = self.client.recv(7331)
            if data_part:
                data.append(data_part.decode())
            else:
                self.client.close()
                break

        return {'message': json.loads(''.join(data).splitlines()[-1]), 'status': int(data[0].split(' ')[1])}

    def _make_request(self, request):
        self._connect()
        self.client.send(request.encode())
        return self._receive()

    def put_user(self, user_id, name_first, name_last=None):
        data = f'{{"name_first":"{name_first}"}}'

        if name_last:
            data = f'{data[:-1]},"name_last":"{name_last}"{data[-1:]}'

        request = f'PUT /put_user/{user_id} HTTP/1.1\r\n' \
                  f'Host:{MOCK_HOST}\r\n' \
                  f'Content-Type: application/json\r\n' \
                  f'Content-Length: {len(data)}\r\n\r\n' \
                  f'{data}\r\n'

        return self._make_request(request)

    def get_user(self, user_id):
        request = f'GET /get_user/{user_id} HTTP/1.1\r\n' \
                  f'Host:{MOCK_HOST}\r\n\r\n'

        return self._make_request(request)

    def delete_user(self, user_id):
        request = f'DELETE /delete_user/{user_id} HTTP/1.1\r\n' \
                  f'Host:{MOCK_HOST}\r\n\r\n'
        
        return self._make_request(request)
