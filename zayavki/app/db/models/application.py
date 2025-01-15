from sqlalchemy import Column, String, Integer, DateTime, func
from zayavki.app.db.base import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=False)
    created_at = Column(DateTime, server_default=func.now())