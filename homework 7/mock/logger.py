from pathlib import Path
import os


class HTTPLogger:
    PATH_LOG_DIR = Path('/tmp/http_client_logs')
    PATH_LOG_REQUEST = PATH_LOG_DIR / 'request.log'
    PATH_LOG_RESPONSE = PATH_LOG_DIR / 'response.log'

    def __init__(self):
        os.makedirs(self.PATH_LOG_DIR, exist_ok=True)

        if os.path.exists(self.PATH_LOG_REQUEST):
            os.remove(self.PATH_LOG_REQUEST)

        if os.path.exists(self.PATH_LOG_RESPONSE):
            os.remove(self.PATH_LOG_RESPONSE)

    def parse_request(self, request):
        info = []
        request = request.splitlines()

        line = request[0].split(' ')
        info.append(f'method: {line[0]}')
        info.append(f'path: {line[1]}')
        info.append(f'version: {line[2]}')

        if line[0] == 'PUT':
            index_empty_line = request.index('')
            info.append('headers:\n\t' + '\n\t'.join(request[1:index_empty_line]))
            info.append('body:\n\t' + '\n\t'.join(request[index_empty_line + 1:]))
        else:
            info.append('headers:\n\t' + '\n\t'.join(request[1:-1]))

        info = '\n'.join(info)
        with open(self.PATH_LOG_REQUEST, 'a') as file:
            file.write(f'{info}\n\n')

    def parse_response(self, response):
        info = []
        # хоть ответы и приходят в виде списков, не догадался, почему они рандомно(?) разбиты по-разному, ...
        # ... поэтому разбиваю самостоятельно
        response = ''.join(response).splitlines()

        line = response[0].split(' ')
        info.append(f'status: {" ".join(line[1:])}')
        info.append(f'version: {line[0]}')

        # не стал делать поправку на то, что headers и body могут отсутствовать, ...
        # ... ибо в работе клиента - это не предусмотрено
        index_empty_line = response.index('')
        info.append('headers:\n\t' + '\n\t'.join(response[1:index_empty_line]))
        info.append('body:\n\t' + '\n\t'.join(response[index_empty_line + 1:]))

        info = '\n'.join(info)
        with open(self.PATH_LOG_RESPONSE, 'a') as file:
            file.write(f'{info}\n\n')
