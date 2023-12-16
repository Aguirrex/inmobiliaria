from fastapi import APIRouter
from models.Contract import Contract as ContractModel
from schemas.ContractSchema import ContractSchema
from utils.common import get_data_router,create_router,delete_router


contract_router = APIRouter()

get_data_router(contract_router,ContractModel,ContractSchema,['contracts'],"/contracts")
create_router(contract_router,ContractModel,ContractSchema,['contracts'],"/contracts/")
delete_router(contract_router,ContractModel,['contracts'],"/contracts/{id}")
