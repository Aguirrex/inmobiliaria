from config.database import Base
from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key = True, index = True)
    price = Column(Float, nullable = False)
    address = Column(String(100), nullable = False)
    available = Column(Boolean, nullable = False)
    description = Column(String(200), nullable = False)

    owner_id = Column(Integer, ForeignKey('owners.id'), nullable = False)
    owner = relationship("Owner", back_populates="properties", uselist=False)

    contracts_property = relationship("Contract", back_populates="property", cascade="all, delete-orphan")

    __table_args__ = (
    ForeignKeyConstraint(['owner_id'], ['owners.id']),
    )
