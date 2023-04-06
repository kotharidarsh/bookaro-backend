from typing import Optional
from pydantic import BaseModel, UUID4, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    emailAddress: EmailStr = None
    fullName: str = None
    organizationId: str = None
    sub: Optional[str] = None
    aud: list = None
    userRole: dict = None
