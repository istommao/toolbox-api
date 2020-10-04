"""user agent parse api."""
from urllib.parse import unquote

from fastapi import FastAPI, Request, APIRouter

from src.responses import Response

from src.toolbox.uaparse import get_ua_parse_result


router = APIRouter()


@router.get('/')
async def parse_ua_api(request: Request):
    w = request.query_params.get('w')

    w = unquote(w)

    result = get_ua_parse_result(w)

    return result
