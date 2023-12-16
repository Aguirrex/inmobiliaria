from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class ContractSchema(BaseModel):

    id : Optional[int] = None
    start_date : str = Field(max_length=10)
    end_date : str = Field(max_length=10)
    property_id : int = Field(ge=1)
    tenant_id : int = Field(ge=1)