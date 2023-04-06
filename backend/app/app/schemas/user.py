from typing import Optional, List

from pydantic import Field, BaseModel, EmailStr, UUID4

from enum import Enum
from datetime import datetime


class UserRole(str, Enum):
    OWNER: str = "Owner"
    MANAGER: str = "Manager"
    USER: str = "User"


class UserBase(BaseModel):
    created_on: Optional[datetime] = datetime.utcnow()
    name: Optional[str] = None
    email_address: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    is_active: Optional[bool] = True
    last_logged_in: Optional[datetime] = datetime.utcnow()
    updated_on: Optional[datetime] = datetime.utcnow()


class UserJwt(BaseModel):
    id: Optional[int] = None
    name: Optional[str]
    email_address: Optional[str]
    phone_number: Optional[str]
    # role: Optional[str] = UserRole.MANAGER.value
    organization_id: Optional[int]
    is_active: Optional[bool] = True


class UserCreate(UserBase):
    name: str
    email_address: Optional[EmailStr]
    phone_number: str
    hashed_password: Optional[str]
    # role: Optional[str] = UserRole.MANAGER.value


class UserUpdate(UserBase):
    hashed_password: Optional[str]
    last_logged_in: Optional[datetime] = datetime.utcnow()
    # role: Optional[str]


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserJwt):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str


class UserAuth(BaseModel):
    emailAddress: EmailStr
    password: str
