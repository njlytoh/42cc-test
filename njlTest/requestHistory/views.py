# Create your views here.

from django.shortcuts import render_to_response
from requestHistory.models import RequestsHistory
from django.core.paginator import Paginator


def history_view(request):
    history = list( reversed ( RequestsHistory.objects.all()) )
    paginated = Paginator( history, 10)
    page_1 = paginated.page(1)
    return render_to_response('requestHistory/history.html', {'links': page_1.object_list })
