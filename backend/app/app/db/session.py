from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

from urllib.parse import quote_plus

SQLALCHEMY_DATABASE_URI: str = f"mysql://{settings.DB_USERNAME}:{quote_plus(settings.DB_PASSWORD)}@" \
                               f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
