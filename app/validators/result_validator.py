from fastapi import HTTPException

from app.models.result_model import LabResult


def validate_result_payload(payload: LabResult) -> None:
    if payload.value < 0:
        raise HTTPException(status_code=422, detail="value must be greater than or equal to 0")
