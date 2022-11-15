from httpx import Response
from .session import Session
from ..settings.settings import API_URL

URL = f'{API_URL}/api/payment-create/'


async def payment_create(price: int, sessionid: str) -> Response:
  return await Session().post(URL, json={'price': price}, cookies={'sessionid': sessionid})
 