"""static page."""
from typing import Optional

from fastapi import FastAPI, Request, APIRouter
from fastapi.templating import Jinja2Templates


router = APIRouter()

templates = Jinja2Templates(directory='html')


@router.get('/')
async def index_page(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})
