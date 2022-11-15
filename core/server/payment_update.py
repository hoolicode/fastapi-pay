from .session import Session
from ..models import Payment
from ..settings.settings import API_URL

from typing import Dict
from httpx import Response

URL = f'{API_URL}/api/payment-update/{{}}/'


async def payment_update(payment: Payment, **kwargs: Dict) -> Response:
  return await Session().patch(URL.format(payment.id), json=kwargs)
