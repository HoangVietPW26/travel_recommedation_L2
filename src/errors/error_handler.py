from fastapi import HTTPException, status


async def validation_error_handler(_request, exc):
    error_details = []
    for error in exc.errors():
        error_details.append({
            "location": ".".join(error['loc']),
            "message": error['msg'],
        })
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail={"error": "Validation Error", "details": error_details},
    )

async def openai_connection_error_handler(_request, _exc):

    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail= "OpenAI Connection Error, check your network or openai_api_key",
    )

async def generic_exception_handler(_request, _exc):
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="An error occurred while processing the recommendation.",
    )
