from fastapi import APIRouter, Path, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from schemas.PropertySchema import PropertySchema
from models.Property import Property as PropertyModel
from config.database import Session
from utils.common import get_data_router, create_router, delete_router
from middlewares.jwt_bearer import JWTBearer


property_router = APIRouter(dependencies=[Depends(JWTBearer())])


get_data_router(property_router,PropertyModel,PropertySchema,['properties'],"/properties")
create_router(property_router,PropertyModel,PropertySchema,['properties'],"/properties/")
delete_router(property_router,PropertyModel,['properties'],"/properties/{id}")


@property_router.get("/properties/{id}",tags=['properties'],response_model=PropertySchema,status_code=200,dependencies=[Depends(JWTBearer())])
def getProperty(id:int = Path(ge=1,le=2000)):

    db = Session()
    result = db.query(PropertyModel).filter(PropertyModel.id == id).first() #porque es json
    response = JSONResponse(content=jsonable_encoder(result),status_code=200)

    if not result:
        response = JSONResponse(content={"message":"property not found"}, status_code=404)

    return response

@property_router.get("/properties/",tags=['properties'],response_model=List[PropertySchema],status_code=200)
def getPropertiesByAvailability(availability : bool): 

    db = Session()
    result = db.query(PropertyModel).filter(PropertyModel.available == availability).all()
    response = JSONResponse(content=jsonable_encoder(result),status_code=200)
    return response


@property_router.put("/properties/{id}",tags=['properties'],response_model=dict,status_code=200)
def updateProperty(id : int, property : PropertySchema):
    db = Session()
    result = db.query(PropertyModel).filter(PropertyModel.id == id).first()

    if not result:
        return JSONResponse(content={"message":"not found"},status_code=404)
    
    result.price = property.price
    result.address = property.address
    result.available = property.available
    result.description = property.description
    result.owner_id = property.owner_id

    db.commit()

    return JSONResponse(content={"message":"property updated successfully"})




