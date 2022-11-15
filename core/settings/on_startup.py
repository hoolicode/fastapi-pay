from ..server import ping

import sys
import logging
from httpx import ConnectError

logger = logging.getLogger(__name__)


async def on_startup() -> None:

  try:
    response = await ping()
    assert response.status_code == 200

  except ConnectError:
    pass

  except AssertionError:
    logger.fatal("Server Credentials are wrong")

  else:
    return

  sys.exit(1)
