"""ip address helper."""

from typing import Optional

from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import PlainTextResponse

from src.toolbox import ipaddr

router = APIRouter()


@router.get('/')
async def ip_is_valid_api(request: Request):
    ip = request.query_params.get('w')

    is_valid = ipaddr.is_valid_ip_address(ip)

    return {'is_valid': is_valid}
