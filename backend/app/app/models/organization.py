from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy import func
from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Organization(Base):

    __tablename__ = "organization"

    id = Column(String, primary_key=True, autoincrement=True, unique=True, index=True)
    created_on = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    name = Column(String)
    location = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    updated_on = Column(
        DateTime, nullable=False, server_default=func.current_timestamp(), server_onupdate=func.current_timestamp())
