from pydantic import BaseModel, Field
from typing import Optional

class TenantSchema(BaseModel):

    id : Optional[int] = None
    nit: int = Field(ge=0)
    name : str = Field(min_length=2,max_length=30)
    lastname : str = Field(min_length=2,max_length=30)
    phone : str = Field(min_length=1, max_length=10)

