from flask import Flask, jsonify, request
from misc.constants import METHOD_GET, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB_NAME, STATUS_OK, STATUS_NOT_FOUND
from mysql.client import MySQLClient
from mysql.models import User

app = Flask(__name__)


@app.route('/vk_id/<user_name>', methods=[METHOD_GET])
def request_get_id(user_name):
    client = MySQLClient(user=MYSQL_USER, password=MYSQL_PASSWORD, db_name=MYSQL_DB_NAME)

    client.connect()
    user = client.session.query(User).filter(User.username == user_name).first()
    client.disconnect()

    if not user:
        return jsonify({}), STATUS_NOT_FOUND

    return jsonify({'vk_id': str(user.id)}), STATUS_OK
