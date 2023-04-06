import base64
from typing import Generator

from fastapi import Depends, HTTPException, status
from jose import jwt
from pydantic import ValidationError

from app import models, schemas
from app.core import security
from app.core.config import settings
from app.core.logger import logger
from app.api.utils.security import OAuth2ClientBearer, oauth2_scheme
from app.db.session import SessionLocal
from sqlalchemy.orm import Session


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    pass


def get_current_active_user(db: Session = Depends(get_db)):
    pass
