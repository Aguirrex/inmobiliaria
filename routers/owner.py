from fastapi import APIRouter, Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from models.Owner import Owner as OwnerModel
from schemas.PropertySchema import PropertySchema
from schemas.OwnerSchema import OwnerSchema
from config.database import Session
from utils.common import get_data_router, create_router, delete_router

owner_router = APIRouter()


get_data_router(owner_router,OwnerModel,OwnerSchema,['owners'],"/owners")
create_router(owner_router,OwnerModel,OwnerSchema,['owners'],"/owners")
delete_router(owner_router,OwnerModel,['owners'],"/owner/{id}")


@owner_router.get("/owners/",tags=['owners'],response_model=OwnerSchema,status_code=200)
def get_owner_by_nit(nit:int = Query(ge=0)):
    db = Session()
    result = db.query(OwnerModel).filter(OwnerModel.nit == nit).first()
    response = JSONResponse(content=jsonable_encoder(result),status_code=200)
    if not result:
        response = JSONResponse(content={"message":"not found"},status_code=404)
    return response


@owner_router.get("/owners/{id}/propierties",tags=['owners'],response_model=List[PropertySchema],status_code=200)
def get_owner_propierties(id:int = Path(ge=1)):
    db = Session()
    owner = db.query(OwnerModel).filter(OwnerModel.nit == id).first()
    if not owner:
        return JSONResponse(content={"message":"not found"},status_code=404)
    propierties = owner.properties
    return JSONResponse(content=jsonable_encoder(propierties),status_code=200)


@owner_router.put("/owners/{id}",tags=['owners'],response_model=dict,status_code=200)
def updateProperty(id : int, owner : OwnerSchema):
    db = Session()
    result = db.query(OwnerModel).filter(OwnerModel.id == id).first()

    if not result:
        return JSONResponse(content={"message":"not found"},status_code=404)
    
    result.nit = owner.nit
    result.name = owner.name
    result.lastname = owner.lastname
    result.phone = owner.phone

    db.commit()

    return JSONResponse(content={"message":"owner updated successfully"})


