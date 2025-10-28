from fastapi.responses import JSONResponse
from fastapi import status as http_status
from fastapi.encoders import jsonable_encoder

def success_response(message: str, data: dict = None, status_code: int = http_status.HTTP_200_OK):
    """
    Standard success response
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "status": 1,
            "message": message,
            "data": jsonable_encoder(data) if data is not None else None
        }
    )

def error_response(message: str, status_code: int = http_status.HTTP_400_BAD_REQUEST):
    """
    Standard error/failure response
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "status": -1,
            "message": message
        }
    )
