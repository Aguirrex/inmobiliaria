from config.database import Base
from sqlalchemy import Column, Integer, Float, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key = True, index = True)
    start_date = Column(String(10), nullable=False)
    end_date = Column(String(10), nullable=False)

    
    property_id = Column(Integer, ForeignKey('properties.id'), nullable = False)
    tenant_id = Column(Integer, ForeignKey('tenants.id'), nullable = False)

    property = relationship("Property", back_populates="contracts_property")
    tenant = relationship("Tenant", back_populates="contracts_tenant")

