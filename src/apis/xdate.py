"""date time helper"""
import time
import datetime

from typing import Optional

from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import PlainTextResponse

from src.toolbox import dateutils

router = APIRouter()


DATETIME_FMT = '%Y-%m-%d %H:%M:%S'
DATE_FMT = '%Y-%m-%d'


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

    return data


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

    return data


@router.get('/dtrange', response_class=PlainTextResponse)
async def datetime_range_api(request: Request):
    """Datetime range api."""
    query_params = request.query_params

    dtstr = query_params.get('w')

    if dtstr == 'day':
        try:
            days = int(query_params.get('days'))
        except (TypeError, ValueError):
            days = 0

        start_at, end_at = dateutils.get_day_range(days=days)
    elif dtstr == 'week':
        try:
            weeks = int(query_params.get('weeks'))
        except (TypeError, ValueError):
            weeks = 0

        start_at, end_at = dateutils.get_week_range(weeks=weeks)
    elif dtstr == 'month':
        try:
            months = int(query_params.get('months'))
        except (TypeError, ValueError):
            months = 0
        start_at, end_at = dateutils.get_month_range(months=months)
    else:
        start_at = end_at = ''

    data = '{}\n{}'.format(start_at, end_at)

    return data
