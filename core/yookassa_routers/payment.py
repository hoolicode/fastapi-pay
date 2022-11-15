from ..server import payment_update
from fastapi import Body, Response


async def payment(data = Body()) -> None:
  payment_id = data['object']['id']

  match data['event']:

    case 'payment.succeeded':
      final_price = data['object']['income_amount']['value']
      await payment_update(payment_id, is_pk=False, **{'paid': True, 'final_price': final_price})

  return Response()
