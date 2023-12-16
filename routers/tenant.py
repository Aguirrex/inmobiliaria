from fastapi import APIRouter
from models.Tenant import Tenant as TenantModel
from schemas.TenantSchema import TenantSchema
from utils.common import get_data_router,create_router,delete_router


tenant_router = APIRouter()

get_data_router(tenant_router,TenantModel,TenantSchema,['tenants'],"/tenants")
create_router(tenant_router,TenantModel,TenantSchema,['tenants'],"/tenants/")
delete_router(tenant_router,TenantModel,['tenants'],"/tenants/{id}")
