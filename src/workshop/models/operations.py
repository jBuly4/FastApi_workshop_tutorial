from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class OperationBase(BaseModel):
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]


class Operation(OperationBase):
    id: int

    class Config:
        orm_mode = True  # that means that we work not with python dicts but with models


class OperationCreate(OperationBase):
    pass  # just for docs and future extensions


class OperationUpdate(OperationBase):
    pass
