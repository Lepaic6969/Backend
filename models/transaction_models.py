from datetime import datetime
from pydantic import BaseModel

class TransactionIn(BaseModel):
    username:str
    value: int

class TransactionOut(BaseModel):
    id_transaction:int
    username: str
    date: datetime
    value:int
    actual_balance:int