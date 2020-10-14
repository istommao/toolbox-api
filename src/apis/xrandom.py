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

    try:
        length = int(length)
    except (ValueError, TypeError):
        length = 6

    if rule == 'digit':
        result = str(xrandom.get_random_number(length))
    else:
        result = xrandom.get_random_string(length)

    return result
