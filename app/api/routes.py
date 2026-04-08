from fastapi import APIRouter

from app.models.result_model import LabResult, ResultResponse
from app.services.result_service import process_result


router = APIRouter()


@router.post("/results", response_model=ResultResponse)
async def create_result(payload: LabResult) -> ResultResponse:
    return process_result(payload)
