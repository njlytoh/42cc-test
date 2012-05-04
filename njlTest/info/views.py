# Create your views here.

from django.shortcuts import render_to_response

from info.models import Info


def info_view(request):
    info = Info.objects.get()
    return render_to_response('info/info.html', {'info': info} )


