from datetime import datetime
from zoneinfo import ZoneInfo

class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Generated-On'] = datetime.now(ZoneInfo('Europe/Berlin')).strftime("%c")
        return response
