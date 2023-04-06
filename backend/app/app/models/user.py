from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Unicode, DateTime
from sqlalchemy.orm import relationship, composite
from sqlalchemy_utils import PhoneNumber
from sqlalchemy import func

from app.db.base_class import Base

if TYPE_CHECKING:
    pass


class User(Base):

    __tablename__ = "user"

    id = Column(String, primary_key=True, autoincrement=True, unique=True, index=True)
    created_on = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    name = Column(String)
    email_address = Column(String, unique=True)
    _phone_number = Column(Unicode(255))
    _country_code = Column(Unicode(8))
    phone_number = composite(
        PhoneNumber,
        _phone_number,
        _country_code
    )
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    last_logged_in = Column(DateTime, default="1970-01-01 00:00:00")
    updated_on = Column(
        DateTime, nullable=False, server_default=func.current_timestamp(), server_onupdate=func.current_timestamp())
