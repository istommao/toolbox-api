"""apis randstr."""
import time

from typing import Optional

from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import PlainTextResponse

from src.toolbox import xrandom

router = APIRouter()


@router.get('/', response_class=PlainTextResponse)
async def xrandom_api(request: Request):
    length = request.query_params.get('len') or 6
    rule = request.query_params.get('rule')
    size = request.query_params.get('size') or 1

    try:
        length = int(length)
    except (ValueError, TypeError):
        length = 6

    try:
        size = int(size)
        if size <= 0:
            size = 1
    except (ValueError, TypeError):
        size = 1

    datalist = []
    for i in range(size):
        if rule == 'digit':
            result = str(xrandom.get_random_number(length))
        else:
            result = xrandom.get_random_string(length)

        datalist.append(result)

    return '\n'.join(datalist)


@router.get('/datetime', response_class=PlainTextResponse)
async def xrandom_datetime_api(request: Request):
    dt_format = request.query_params.get('format')
    size = request.query_params.get('size') or 1


    try:
        size = int(size)
        if size <= 0:
            size = 1
    except (ValueError, TypeError):
        size = 1

    datalist = []
    for i in range(size):
        result = xrandom.get_random_datetime(dt_format)

        datalist.append(result)

    return '\n'.join(datalist)
