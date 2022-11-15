from ..server import payment_update

import logging
from fastapi import Body, Response

logger = logging.getLogger(__name__)


async def payment(data = Body()) -> None:
  payment_id = data['object']['id']

  match (event := data['event']):

    case 'payment.succeeded':
      final_price = data['object']['income_amount']['value']
      await payment_update(payment_id, is_pk=False, **{'paid': True, 'final_price': final_price})

    case 'payment.canceled':
      await payment_update(payment_id, is_pk=False, **{'cancelled': True})

    case _:
      logger.error(f'Unregistered event: {event}')

  return Response()
