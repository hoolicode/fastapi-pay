from fastapi import FastAPI
from .on_startup import on_startup

application = FastAPI()
application.add_event_handler('startup', on_startup)
