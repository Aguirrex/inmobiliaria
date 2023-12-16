from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint
from sqlalchemy.orm import relationship

class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key = True, index = True)
    nit = Column(Integer,unique=True)
    name = Column(String(30), nullable = False)
    lastname = Column(String(30), nullable = False)
    phone = Column(String(10), nullable = False)

    properties = relationship("Property", back_populates="owner", cascade="all, delete-orphan")
    

