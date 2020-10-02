from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.routers import ROUTER_CONFIG

app = FastAPI()


app.mount('/static', StaticFiles(directory='static'), name='static')


def load_routers(app):
    for router, config in ROUTER_CONFIG:
        app.include_router(router, **config)


load_routers(app)
