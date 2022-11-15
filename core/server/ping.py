from httpx import Response
from .session import Session
from ..settings.settings import API_URL

URL = f'{API_URL}/api/ping/'


async def ping() -> Response:
  return await Session().get(URL)
