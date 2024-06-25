from fastapi import APIRouter, HTTPException
from fast_api_app.models.addition_models import AdditionRequest, AdditionResponse
from fast_api_app.services.addition_service import perform_addition
from fast_api_app.utils.logger import logger

router = APIRouter()

@router.post("/add", response_model=AdditionResponse)
def add_numbers(request: AdditionRequest) -> AdditionResponse:
    try:
        logger.info(f"Received request: {request.json()}")
        result = perform_addition(request.payload)
        response = AdditionResponse(batchid=request.batchid, **result)
        logger.info(f"Sending response: {response.json()}")
        return response
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
