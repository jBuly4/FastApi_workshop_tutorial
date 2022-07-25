# endpoint for operations
from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status

from ..models.operations import Operation, OperationKind, OperationCreate, OperationUpdate
from ..services.auth import get_current_user, User
from ..services.operations import OperationService


router = APIRouter(
        prefix='/operations',  # all handlers will work at paths path_from_root/operations/
)


# @router.get('/', response_model=List[Operation])
# def get_operations():
#     session = Session()
#     operations = (
#         session.query(tables.Operation).all()
#     )
#
#     return operations
# mistake in code above is that we don't close session. we should use session.close() but we have to write it in
# every handler so instead of that we can create method in databases get_session()
# then with help of magic class Depends that will help to implement new dependencies in our code (callable objects,
# # generators, asynchronous funcs and generators
#
# @router.get('/', response_model=List[Operation])
# def get_operations(session: Session = Depends(get_session)):
#     operations = (
#         session.query(tables.Operation).all()
#     )
#     return operations
# let's move our business logic to services

# @router.get('/', response_model=List[Operation])
# def get_operations(service: OperationService = Depends()):
#     return service.get_list()

# let's show how to work with parameters in queries
# import OperationKind
# request is get then parameters will be taken not from body of request
# in url there are no variables for parameters so parameters are not a part of url
# last way is to take params from query string
# in docs of api you will see field where you need to choose filter
@router.get('/', response_model=List[Operation])
def get_operations(
        kind: Optional[OperationKind] = None,
        user: User = Depends(get_current_user),
        service: OperationService = Depends()
):
    return service.get_list(user_id=user.id, kind=kind)


@router.get('/{operation_id}', response_model=Operation)
def get_operation(
        operation_id: int,
        user: User = Depends(get_current_user),
        service: OperationService = Depends()
):
    return service.get(user_id=user.id, operation_id=operation_id)


# need to refactor models
@router.post('/', response_model=Operation)
def create_operation(
        operation_data: OperationCreate,
        user: User = Depends(get_current_user),
        service: OperationService = Depends()
):
    return service.create(user_id=user.id, operation_data=operation_data)


@router.put('/{operation_id}', response_model=Operation)
def update_operation(
        operation_id: int,
        operation_data: OperationUpdate,
        user: User = Depends(get_current_user),
        service: OperationService = Depends()
):
    return service.update(user_id=user.id, operation_id=operation_id, operation_data=operation_data)


@router.delete('/{operation_id}')
def delete_operation(
        operation_id: int,
        user: User = Depends(get_current_user),
        service: OperationService = Depends()
):
    service.delete(user_id=user.id, operation_id=operation_id)
    # we need to return empty response. if we don't then will be a mistake because fastapi will try to return json
    return Response(status_code=status.HTTP_204_NO_CONTENT)
