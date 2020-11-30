"""url utils."""
import re

from urllib.parse import quote, urlparse, parse_qsl, urlencode

URL_REGEX = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
    r'localhost|' # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


URL_PATTERN = re.compile(URL_REGEX)


def is_vaild_url(value):
    """is valid url"""
    result = URL_PATTERN.match(value)

    return True if result else False


def url_quote(raw_url: str):
    """Url quote."""
    if not is_vaild_url(raw_url):
        return quote(raw_url)

    parse_result = urlparse(raw_url)

    query = '?' + urlencode(
        dict(parse_qsl(parse_result.query))
    ) if parse_result.query else ''

    fragment = '#' + quote(parse_result.fragment) if parse_result.fragment else ''

    full_path = '{scheme}://{hostname}{path}{query}{fragment}'.format(
        scheme=parse_result.scheme,
        hostname=parse_result.netloc,
        path=quote(parse_result.path),
        query=query,
        fragment=fragment
    )

    return full_path
