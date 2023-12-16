from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from schemas.PropertySchema import PropertySchema
from models.Property import Property as PropertyModel
from config.database import Session

def get_data_router(router:APIRouter,model,schema,tags,endpoint):

    @router.get(endpoint,tags=tags,response_model=List[schema],status_code=200)
    def get_data() -> List[schema]:

        db = Session()
        result = db.query(model).all()

        return JSONResponse(content=jsonable_encoder(result),status_code=200)
    

def create_router(router:APIRouter,model,schema,tags,endpoint):
    @router.post(endpoint,tags=tags,response_model=dict,status_code=201)
    def create(entity:schema):
        db = Session()
        new_data = model(**entity.model_dump())
        db.add(new_data)
        db.commit()
        
        return JSONResponse(content={"message": "created successfully"},
                            status_code=201)

def delete_router(router:APIRouter,model,tags,endpoint):
    @router.delete(endpoint,tags=tags,response_model=dict)
    def delete(id : int):
        db = Session()
        result = db.query(model).filter(model.id == id).first()
        response = JSONResponse(content=jsonable_encoder(result))
        if not result:
            return JSONResponse(content={"message":"not found"})
        db.delete(result)
        db.commit()
        return response