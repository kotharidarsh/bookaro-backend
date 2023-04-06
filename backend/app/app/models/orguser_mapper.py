from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, String, DateTime, ForeignKey, Integer
from sqlalchemy import func
from app.db.base_class import Base
from sqlalchemy.orm import composite, relationship

if TYPE_CHECKING:
    from .organization import Organization  # noqa: F401
    from .rolemaster import RoleMaster  # noqa: F401
    from .user import User  # noqa: F401


class OrgUserMapper(Base):

    __tablename__ = "orguser_mapper"

    id = Column(String, primary_key=True, autoincrement=True, unique=True, index=True)
    created_on = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    fk_org_id = Column(Integer, ForeignKey("organization.id"))
    fk_user_id = Column(Integer, ForeignKey("user.id"))
    fk_role_id = Column(Integer, ForeignKey("rolemaster.id"))
    is_active = Column(Boolean, default=True)
    updated_on = Column(
        DateTime, nullable=False, server_default=func.current_timestamp(), server_onupdate=func.current_timestamp())

    # defining relationship
    user = relationship("User", back_populates="")
    organization = relationship("Organization", back_populates="")
    roles = relationship("RoleMaster", back_populates="")