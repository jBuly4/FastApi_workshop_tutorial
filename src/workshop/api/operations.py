# endpoint for operations
from typing import List
from fastapi import APIRouter

from ..models.operations import Operation

router = APIRouter(
        prefix='/operations',  # all handlers will work at paths path_from_root/operations/
)


@router.get('/', response_model=List[Operation])
def get_operations():
    return []