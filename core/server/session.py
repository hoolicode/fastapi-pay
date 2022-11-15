from ..utils import Singleton
from ..settings.settings import API_TOKEN

import logging
from functools import wraps
from fastapi import HTTPException, status
from typing import Coroutine, Tuple, Dict
from httpx import AsyncClient, Response, ConnectError

logger = logging.getLogger(__name__)


def catch_exceptions(coroutine: Coroutine) -> Coroutine:

  @wraps(coroutine)
  async def wrapper(*args: Tuple, **kwargs: Dict) -> Response:

    try:
      response = await coroutine(*args, **kwargs)
    except ConnectError:
      logger.fatal("Can't connect to the server")
      raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, 'The Server is down')

    return response

  return wrapper


class Session(AsyncClient, metaclass=Singleton):

  def __init__(self, *args: Tuple, headers: Dict = dict(), **kwargs: Dict) -> None:
    headers['Authorization'] = API_TOKEN
    return super().__init__(*args, headers=headers, **kwargs)

  @catch_exceptions
  async def get(self, *args: Tuple, **kwargs: Dict) -> Response:
    return await super().get(*args, **kwargs)

  @catch_exceptions
  async def post(self, *args: Tuple, **kwargs: Dict) -> Response:
    return await super().post(*args, **kwargs)

  @catch_exceptions
  async def patch(self, *args: Tuple, **kwargs: Dict) -> Response:
    return await super().patch(*args, **kwargs)
