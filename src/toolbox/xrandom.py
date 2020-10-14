"""toolbox xrandom."""
import random


def get_random_string(
    length, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    length = int(length)
    return ''.join(random.choice(allowed_chars) for i in range(length))


def get_random_number(length):

    return random.randint(
        10 ** (length - 1), 10 ** length - 1
    )
