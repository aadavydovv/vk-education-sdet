import random
import string


def make_username():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16))


def make_email(username):
    return f'{username}@mail.ru'
