"""routers map"""
from src.apis import page, xdate, fdata, ipaddr


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
    )
]
