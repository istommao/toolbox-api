"""fake user agent."""

from fastapi import FastAPI, Request, APIRouter

from src.responses import Response

from src.toolbox.fakeua import FakeUserAgent

router = APIRouter()


@router.get('/')
async def get_user_agent_api(request: Request):
    w = request.query_params.get('w')
    media_type = request.query_params.get('format')
    browser = request.query_params.get('browser')

    user_agent = FakeUserAgent().random_one(browser=browser)

    data = f'{user_agent}' if media_type == 'text' else {'user_agent': user_agent}

    return Response(data, media_type=media_type)
