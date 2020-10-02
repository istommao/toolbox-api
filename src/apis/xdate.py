"""date time helper"""
import time
import datetime

from typing import Optional

from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import PlainTextResponse

from src.toolbox import dateutils

router = APIRouter()


DATETIME_FMT = '%Y-%m-%d %H:%M:%S'


@router.get('/')
async def xdate_api(request: Request):
    # result = {*dir(request)}

    return {'Description': 'datetime tools'}


@router.get('/ts', response_class=PlainTextResponse)
async def ts_to_datetime_api(request: Request):
    ts = request.query_params.get('w')
    if ts == 'now':
        ts = int(time.time())

    try:
        datetime_obj = dateutils.ts_to_datetime(int(ts))
        data = str(datetime_obj)
    except (TypeError, ValueError):
        data = '-'

    return data + '\n'


@router.get('/dt', response_class=PlainTextResponse)
async def datetime_to_ts_api(request: Request):
    dtstr = request.query_params.get('w')
    if dtstr == 'now':
        data = str(int(time.time()))
    else:
        try:
            dtobj = datetime.datetime.strptime(dtstr, DATETIME_FMT)

            data = str(dateutils.datetime_to_ts(dtobj))
        except (TypeError, ValueError):
            data = '-'

    return data + '\n'
