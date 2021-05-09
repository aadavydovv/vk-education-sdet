#!/usr/bin/env python3

from pathlib import Path
import argparse
import collections
import json

PATH_DIR_OUTPUT = Path('/tmp/parsed_log')

parser = argparse.ArgumentParser()
parser.add_argument('--file', default='../misc/access.log')
parser.add_argument('--json', action='store_true')
args = parser.parse_args()
path_file_log = Path(__file__).parents[1] / args.file

PATH_DIR_OUTPUT.mkdir(exist_ok=True)
string_output = ''

with open(path_file_log) as file_log:
    lines_log = [line.split(' ') for line in file_log.readlines()]

string_output += f'Общее количество запросов\n'
amount_requests_overall = len(lines_log)
string_output += str(amount_requests_overall)
                 
string_output += '\n\nОбщее количество запросов по типу\n'
amount_requests_by_type = collections.defaultdict(lambda: 0)
for line in lines_log:
    amount_requests_by_type[line[5][1:]] += 1
string_output += '\n'.join([f'{type} - {amount_requests_by_type[type]}' for type in amount_requests_by_type])

string_output += '\n\nТоп 10 самых частых запросов\n'
top_by_url = collections.Counter([line[6] for line in lines_log]).most_common(10)
string_output += '\n'.join([f'{request[0]} - {request[1]}' for request in top_by_url])

string_output += '\n\nТоп 5 самых больших по размеру запросов, которые завершились клиентской ошибкой\n'
lines_log_formatted = [[line[6], line[8], int(line[9]), line[0]] for line in lines_log if line[8].startswith('4')]
top_by_size_with_client_error = sorted(lines_log_formatted, key=lambda x: (x[2]), reverse=True)[:5]
string_output += '\n'.join([' - '.join([str(line) for line in line]) for line in top_by_size_with_client_error])

string_output += '\n\nТоп 5 пользователей по количеству запросов, которые завершились серверной ошибкой\n'
lines_log_formatted = [line[0] for line in lines_log if line[8].startswith('5')]
top_by_ip_with_server_error = collections.Counter(lines_log_formatted).most_common(5)
string_output += '\n'.join([f'{entry[0]} - {entry[1]}' for entry in top_by_ip_with_server_error])

if args.json:
    json_output = {
        'requests_overall': amount_requests_overall,
        'requests_by_type': amount_requests_by_type,
        'top_by_url': [{'url': entry[0], 'requests': int(entry[1])} for entry in top_by_url],
        'top_by_size_with_client_error': [{'url': entry[0], 'code': int(entry[1]), 'size': entry[2], 'ip': entry[3]}
                                          for entry in top_by_size_with_client_error],
        'top_by_ip_with_server_error': [{'ip': entry[0], 'requests': entry[1]} for entry in top_by_ip_with_server_error]
    }

    with open(PATH_DIR_OUTPUT / 'by_python.json', 'w') as file_output:
        json.dump(json_output, file_output)

with open(PATH_DIR_OUTPUT / 'by_python', 'w') as file_output:
    file_output.write(string_output + '\n')
