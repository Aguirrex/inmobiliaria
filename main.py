from fastapi import FastAPI
from config.database import Base, engine

from routers.owner import owner_router
from routers.property import property_router
from routers.tenant import tenant_router
from routers.contract import contract_router
from routers.auth import auth_router

from middlewares.error_handler import ErrorHandler

app = FastAPI()
app.title = "API INMOBILIARIA"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

app.include_router(owner_router)
app.include_router(property_router)
app.include_router(contract_router)
app.include_router(tenant_router)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)
