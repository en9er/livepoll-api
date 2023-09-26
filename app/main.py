import logging.config

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.events.create_database_event import create_database, migrate
from app.core.events import database_connection_event as db_conn
from app.routes.user_route import user_router


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

logging.config.dictConfig(LOGGING_CONFIG)

app = FastAPI()

origins = [
    "http://localhost:4200",
    "http://localhost:4201",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.add_event_handler("startup", create_database())
app.add_event_handler("startup", migrate())
app.add_event_handler("startup", db_conn.start())
app.add_event_handler("shutdown", db_conn.stop())


app.include_router(user_router, prefix="/api")
