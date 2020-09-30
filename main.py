from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src import static_page

app = FastAPI()


app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(static_page.router)
