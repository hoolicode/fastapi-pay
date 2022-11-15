from fastapi import FastAPI
from .on_startup import on_startup
from ..yookassa_routers import router as yookassa_router

application = FastAPI()
application.add_event_handler('startup', on_startup)

application.include_router(yookassa_router)
