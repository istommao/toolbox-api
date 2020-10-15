"""toolbox xrandom."""
import datetime
import time

import random


def get_random_string(
    length, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    length = int(length)
    return ''.join(random.choice(allowed_chars) for i in range(length))


def get_random_number(length):

    return random.randint(
        10 ** (length - 1), 10 ** length - 1
    )


def get_random_datetime(datetime_format):

    if datetime_format == 'ts':
        result = int(time.time())
    else:
        result = str(datetime.datetime.now())

    return result
