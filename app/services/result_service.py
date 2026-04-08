from app.events.event_handler import on_result_received
from app.models.result_model import LabResult, ResultResponse
from app.validators.result_validator import validate_result_payload


def process_result(payload: LabResult) -> ResultResponse:
    validate_result_payload(payload)
    on_result_received(payload)
    return ResultResponse(status="ok", received=payload)
