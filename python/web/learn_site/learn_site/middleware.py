import logging
import time

logger = logging.getLogger(__name__)


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        before_timestamp = time.time()

        response = self.get_response(request)
        
        after_timestamp = time.time()
        delta = after_timestamp - before_timestamp

        logger.info(f"Time delte: {delta}")

        return response
    
    def proccess_view(self, request, view_func, view_args, view_kwargs):
        logger.info(
            f"Running {view_func.__name__} view"
        )
