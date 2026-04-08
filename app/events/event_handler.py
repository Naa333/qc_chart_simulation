import logging

from app.models.result_model import LabResult


logger = logging.getLogger(__name__)


def on_result_received(payload: LabResult) -> None:
    logger.info(
        "Received result for test_name=%s from instrument_id=%s",
        payload.test_name,
        payload.instrument_id,
    )
