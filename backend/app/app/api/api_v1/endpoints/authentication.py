from fastapi import FastAPI, APIRouter, status, Body, Depends, HTTPException
from fastapi.responses import JSONResponse
from urllib.parse import urlparse

from datetime import timedelta, datetime, date
from typing import Any

from app.api import deps
from sqlalchemy.orm import Session
from app.schemas.user import UserAuth

from fastapi.security import OAuth2PasswordRequestForm

from app.core import security

from app.core.config import settings
from app.core.logger import logger
from app import crud, models, schemas, tasks
import hashlib
import traceback
import json

router = APIRouter()


@router.post('/login', summary='Generates Access Token', response_model=schemas.Token)
async def login(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    """

    :param db:
    :param form_data:
    :return:
    """
    pass
