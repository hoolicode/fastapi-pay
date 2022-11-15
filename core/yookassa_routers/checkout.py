from httpx import ConnectError
from ..server import payment_create

from typing import Dict
from fastapi.responses import ORJSONResponse
from fastapi import Body, Cookie, HTTPException, status


async def checkout(price: int = Body(embed=True), sessionid: str = Cookie()) -> Dict:

  try:
    response = await payment_create(price, sessionid)
  except ConnectError:
    raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, 'The Server is down')

  match response.status_code:

    case 201:
      return ORJSONResponse(response.json(), status.HTTP_201_CREATED)

    case 403:
      raise HTTPException(status.HTTP_403_FORBIDDEN, response.json())

    case _:
      return ORJSONResponse(response.json(), status.HTTP_400_BAD_REQUEST)
