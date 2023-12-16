from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key = True, index=True)
    nit = Column(Integer,unique=True)
    name = Column(String(30), nullable = False)

    lastname = Column(String(30), nullable = False)
    phone = Column(String(10), nullable = False)

    contracts_tenant = relationship("Contract", back_populates="tenant", cascade="all, delete-orphan")
