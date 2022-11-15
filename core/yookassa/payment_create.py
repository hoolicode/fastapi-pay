from ..models import Payment

from httpx import Response
from .session import Session
from ..settings.settings import YOOKASSA_URL

URL = f'{YOOKASSA_URL}/payments/'


async def payment_create(payment: Payment, return_url: str, description: str) -> Response:
  session = Session()

  response = await session.post(
    URL,
    headers={'Idempotence-Key': str(payment.idempotence_key)},
    json={
      'amount': {
        'value': payment.price,
        'currency': 'RUB'
      },
      'confirmation': {
        'type': 'redirect',
        'return_url': return_url
      },
      'capture': True,
      'description': description
    }
  )

  return response
