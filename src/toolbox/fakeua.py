"""user agent"""
from fake_useragent import UserAgent


class FakeUserAgent:

    def __init__(self):
        self.__ua = UserAgent()

    def random_one(self):
        return self.__ua.random
