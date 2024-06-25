from pydantic import BaseModel
from typing import List

class AdditionRequest(BaseModel):
    batchid: str
    payload: List[List[int]]

class AdditionResponse(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: str
    completed_at: str
