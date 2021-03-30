import random
import string


def get_random_email():
    return ['user', random.randint(1, 1337), '@mail.domain']


def get_random_fio():
    fio = []
    for _ in range(3):
        fio += [''.join([random.choice(string.ascii_uppercase)] +
                        random.choices(string.ascii_lowercase, k=random.randint(4, 8)))]

    return ' '.join(fio)


def get_random_phone():
    return f'{"+7"}{random.randint(10 ** 9, 10 ** 10 - 1)}'
