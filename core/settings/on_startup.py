from .settings import API_URL

import sys
import logging
from httpx import AsyncClient, ConnectError

logger = logging.getLogger(__name__)


async def on_startup() -> None:
  async with AsyncClient() as session:

    try:
      request = await session.get(f'{API_URL}/api/ping/')
      assert request.status_code == 200
    except (ConnectError, AssertionError):
      logger.fatal("Something's wrong with the server")
      sys.exit(1)
