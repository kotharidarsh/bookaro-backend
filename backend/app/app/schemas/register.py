from typing import Optional
from pydantic import BaseModel, EmailStr

from enum import Enum


class RegisterOrganizationAndUser(BaseModel):
    userFullName: str
    userPhoneNumber: str
    userEmailAddress: EmailStr = "user@example.com"
    password: str
    orgName: str = "Example"
    orgLocation: Optional[str] = "Mumbai"

    # @validator("userPhoneNumber")
    # def phone_validation(cls, v):
    #     logger.debug(f"phone in 2 validator:{v}")
    #     regex = r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$"
    #     if v and not re.search(regex, v, re.I):
    #         raise ValueError("Phone Number Invalid.")
    #     return v

    class Config:
        orm_mode = False
        use_enum_values = True
