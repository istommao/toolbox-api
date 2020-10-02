"""fake data helper."""
import time

from typing import Optional

from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import PlainTextResponse

from src.toolbox import dateutils

router = APIRouter()


@router.get('/')
async def fdata_api(request: Request):
    return {'Description': 'fake data tools'}


@router.get('/list')
async def fdata_list_api(request: Request):
    fields = request.query_params.get('fields') or ''
    fields = fields.replace(' ', '')

    field_list = fields.split(',')

    return field_list
