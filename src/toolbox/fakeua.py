"""user agent"""
from fake_useragent import UserAgent


class FakeUserAgent:

    def __init__(self):
        self.__ua = UserAgent()

        self.browser_map = {
            'ie': self.__ua.ie,
            'msie': self.__ua.msie,
            'ff': self.__ua.ff,
            'opera': self.__ua.opera,
            'chrome': self.__ua.chrome,
            'safari': self.__ua.safari,
            'firefox': self.__ua.firefox,
            'google': self.__ua.google
        }

    def random_one(self, browser=None):
        specify_browser = self.browser_map.get(browser, self.__ua.random)

        return specify_browser
