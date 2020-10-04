"""routers map"""
from src.apis import page, xdate, fdata, ipaddr, fakeua, uaparse


ROUTER_CONFIG = [
    (page.router, {}),
    (
        xdate.router,
        {
            'prefix': '/api/dateutils',
            'tags': ['datetime'],
            'responses': {404: {'description': '404 Not found'}}
        }
    ),
    (
        fdata.router,
        {
            'prefix': '/api/fdata',
            'tags': ['fakedata'],
            'responses': {404: {'description': '404 Not found'}}
        }
    ),
    (
        ipaddr.router,
        {
            'prefix': '/api/ipaddr',
            'tags': ['ipaddr'],
            'responses': {404: {'description': '404 Not found'}}
        }
    ),
    (
        fakeua.router,
        {
            'prefix': '/api/fakeua',
            'tags': ['fakeua'],
            'responses': {404: {'description': '404 Not found'}}
        }
    ),
    (
        uaparse.router,
        {
            'prefix': '/api/uaparse',
            'tags': ['uaparse'],
            'responses': {404: {'description': '404 Not found'}}
        }
    )
]
