import logging
from rest_framework.views import APIView

logger = logging.getLogger("django")
error_logger = logging.getLogger('error_logger')

class AuditLogMixin(APIView):
    def finalize_response(self, request, response, *args, **kwargs):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_str = f'User: {user} | Method: {request.method} | Path: {request.path} | Status: {response.status_code} | IP: {request.META.get("REMOTE_ADDR")}'
        logger.info(log_str)
        print(log_str)
        return super().finalize_response(request, response, *args, **kwargs)

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        user = self.request.user if self.request.user.is_authenticated else "Anonymous"
        log_str = (
            f"Error: {str(exc)} | User: {user} | Method: {self.request.method} | "
            f"Path: {self.request.path} | Status: {response.status_code} | "
            f'IP: {self.request.META.get("REMOTE_ADDR")}'
        )
        error_logger.error(log_str)
        print(log_str)
        return response
