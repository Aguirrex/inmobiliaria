from pydantic import BaseModel, Field
from typing import Optional

class PropertySchema(BaseModel):

    id : Optional[int] = None
    price : float = Field(ge=0)
    address : str = Field(min_length=10,max_length=100)
    available : bool
    description : str = Field(min_length=5,max_length=200)
    owner_id : int = Field(ge=1)
