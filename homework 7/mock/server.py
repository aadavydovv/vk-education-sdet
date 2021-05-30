from flask import Flask, jsonify, request
from mock.constants import *
import threading

app = Flask(__name__)
users = {}


def run():
    threading.Thread(target=app.run, kwargs={'host': MOCK_HOST, 'port': MOCK_PORT}).start()


@app.route('/shutdown')
def request_shutdown():
    function = request.environ.get('werkzeug.server.shutdown')
    if function:
        function()

    return jsonify(f'shutting down...'), STATUS_OK


@app.route('/get_user/<user_id>', methods=['GET'])
def request_get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify(f'a user with id "{user_id}" does not exist'), STATUS_ERROR

    name_first = user.get('name_first')
    name_last = user.get('name_last')

    message = {'name_first': name_first}
    if name_last:
        message['name_last'] = name_last

    return jsonify(message), STATUS_OK


@app.route('/put_user/<user_id>', methods=['PUT'])
def request_put_user(user_id):
    data = request.get_json()
    name_first = data.get('name_first')
    name_last = data.get('name_last')

    if user_id in users:
        if not (name_first or name_last):
            return jsonify(f'to edit a user a request needs at least a first or a last name'), STATUS_BAD_REQUEST

        status = STATUS_OK

    else:
        if not name_first:
            return jsonify(f'a new user should at least have a first name'), STATUS_BAD_REQUEST

        status = STATUS_CREATED

    users[user_id] = {}
    message = {'id': user_id}

    if name_first:
        users[user_id]['name_first'] = name_first
        message['name_first'] = name_first

    if name_last:
        users[user_id]['name_last'] = name_last
        message['name_last'] = name_last

    return jsonify(message), status


@app.route('/delete_user/<user_id>', methods=['DELETE'])
def request_delete_user(user_id):
    if user_id in users:
        user = users.pop(user_id)

        user_data = {'id': user_id}

        user_name_first = user.get('name_first')
        if user_name_first:
            user_data['name_first'] = user_name_first

            user_name_last = user.get('name_last')
            if user_name_last:
                user_data['name_last'] = user_name_last

        return jsonify(user_data), STATUS_OK

    else:
        return jsonify(f'a user with id "{user_id}" does not exist'), STATUS_ERROR


@app.route('/post_user/<user_id>', methods=['POST'])
def request_post_user(user_id):
    if user_id in users:
        return jsonify(f'the user with id \"{user_id}\" already exists'), STATUS_ERROR

    data = request.get_json()

    name_first = data.get('name_first')
    if not name_first:
        return jsonify(f'a \"post_user\" request needs at least a first name'), STATUS_BAD_REQUEST

    name_last = data.get('name_last')

    users[user_id] = {}
    message = {'id': user_id}

    users[user_id]['name_first'] = name_first
    message['name_first'] = name_first

    if name_last:
        users[user_id]['name_last'] = name_last
        message['name_last'] = name_last

    return jsonify(message), STATUS_CREATED
