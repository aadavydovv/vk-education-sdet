#!/usr/bin/env python3

from pathlib import Path
import argparse

TYPES_REQUESTS = ('GET', 'POST', 'PUT', 'HEAD', 'DELETE', 'PATCH', 'OPTION')
PATH_DIR_OUTPUT = Path('/tmp/parsed_log')
PATH_FILE_OUTPUT = PATH_DIR_OUTPUT / 'by_python'


def get_amount_requests_by_type(type_request, file):
    amount = sum(f'] \"{type_request}' in line for line in file)
    file.seek(0)
    return amount


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='../misc/access.log')
    args = parser.parse_args()
    path_file_log = Path(__file__).parents[1] / args.file

    PATH_DIR_OUTPUT.mkdir(exist_ok=True)
    output_string = ''

    with open(PATH_FILE_OUTPUT, 'w') as file_output:
        with open(path_file_log) as file_log:
            output_string += 'Общее количество запросов\n'
            output_string += f'{sum(get_amount_requests_by_type(tr, file_log) for tr in TYPES_REQUESTS)}\n'

            output_string += '\nОбщее количество запросов по типу\n'
            for type_request in TYPES_REQUESTS:
                output_string += f'{type_request} - {get_amount_requests_by_type(type_request, file_log)}\n'

            file_output.write(output_string)


if __name__ == '__main__':
    main()
