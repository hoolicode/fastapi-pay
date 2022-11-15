from ..utils import Singleton
from ..settings.settings import YOOKASSA_ID, YOOKASSA_TOKEN

from typing import Tuple, Dict
from httpx import AsyncClient, BasicAuth


class Session(AsyncClient, metaclass=Singleton):

  def __init__(self, *args: Tuple, **kwargs: Dict) -> None:
    kwargs.setdefault('auth', BasicAuth(YOOKASSA_ID, YOOKASSA_TOKEN))
    return super().__init__(*args, **kwargs)
