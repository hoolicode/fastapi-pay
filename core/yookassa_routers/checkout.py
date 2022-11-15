from ..models import Payment
from ..yookassa import payment_create as yookassa_payment_create

from ..server import payment_create as server_payment_create
from ..server import payment_update as server_payment_update

import logging
from typing import Dict
from httpx import ConnectError
from pydantic import BaseModel, AnyUrl
from fastapi.responses import ORJSONResponse
from fastapi import Cookie, HTTPException, status

logger = logging.getLogger(__name__)


class Data(BaseModel):
  price: float
  return_url: AnyUrl


async def checkout(data: Data, sessionid: str = Cookie()) -> Dict:
  response = await server_payment_create(data.price, sessionid)

  payment = Payment(**response.json())
  response = await yookassa_payment_create(payment, data.return_url)

  if response.status_code != 200:
    logger.error(f"YooKassa can't generate a payment\n{response.json()}")
    raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, 'YooKassa Server is unavailable')

  response = await server_payment_update(payment, payment_id=response.json()['id'])
  response_json = response.json()

  return ORJSONResponse({'return_url': response_json['confirmation_url']})
