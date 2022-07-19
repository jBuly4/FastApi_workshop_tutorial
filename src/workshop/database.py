from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

engine = create_engine(
        settings.database_url,
        connect_args={'check_same_thread': False},  # fastapi is asynchronious but sqlite is not, so we need to be
        # sure that sqlit will be used in synchronious way, i.e. one request - one session
)

Session = sessionmaker(
        engine,
        autoflush=False,
        autocommit=False,
)
