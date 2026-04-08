from datetime import datetime

from pydantic import BaseModel


class LabResult(BaseModel):
    test_name: str
    value: float
    unit: str
    timestamp: datetime
    instrument_id: str


class ResultResponse(BaseModel):
    status: str
    received: LabResult
