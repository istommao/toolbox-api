"""user agent parse."""
from user_agents import parse


def get_ua_parse_result(ua_string):
    data = parse(ua_string)

    result = {
        'name': data.browser.family,
        'version': data.browser.version_string,
        'os': data.get_os(),
        'device': data.get_device()
    }

    return result
