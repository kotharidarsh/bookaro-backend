from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy import func
from app.db.base_class import Base

if TYPE_CHECKING:
    pass


class RoleMaster(Base):

    __tablename__ = "role_master"

    id = Column(String, primary_key=True, autoincrement=True, unique=True, index=True)
    created_on = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    name = Column(String)
    is_active = Column(Boolean, default=True)
    updated_on = Column(
        DateTime, nullable=False, server_default=func.current_timestamp(), server_onupdate=func.current_timestamp())
