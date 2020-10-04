"""customer responses."""

from fastapi.encoders import jsonable_encoder
from fastapi.responses import PlainTextResponse, JSONResponse


class Response:

    def __new__(cls, data, media_type='json'):
        if media_type == 'text':
            return PlainTextResponse(content=str(data))
        else:
            return JSONResponse(content=jsonable_encoder(data))
