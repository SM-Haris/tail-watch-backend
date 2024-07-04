from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

error_logger = logging.getLogger('error_logger')

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return response

    error_logger.error(f"Unhandled error: {exc}", exc_info=True)

    custom_response_data = {"detail": "Something went wrong. Please try again later."}

    return Response(custom_response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
