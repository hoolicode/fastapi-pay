from .session import Session
from ..settings.settings import API_URL

from uuid import UUID
from httpx import Response
from typing import Union, Dict

URL_PK = f'{API_URL}/api/payment-update/pk/{{}}/'
URL_UUID = f'{API_URL}/api/payment-update/uuid/{{}}/'


async def payment_update(lookup_field: Union[str, UUID], is_pk: bool = True, **kwargs: Dict) -> Response:

  if is_pk:
    url = URL_PK.format(lookup_field)
  else:
    url = URL_UUID.format(lookup_field)

  return await Session().patch(url.format(lookup_field), json=kwargs)
