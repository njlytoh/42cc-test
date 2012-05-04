
from requestHistory.models import RequestsHistory

class BeforeFilter(object):
    def process_request(self, request):
        settings.my_var = 'Hello World'
        return None

class HistoryMiddleware(object):
    def process_request(self, request):
        history = RequestsHistory()
        history.url = request.build_absolute_uri()
        history.post = repr(request.POST)
        history.get = repr(request.GET)
        history.save()
