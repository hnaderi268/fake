from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world")

def time(request):
    now=datetime.datetime.now()
    return render(request,'time.html',Context({'time':now}))

def timeP(request, plus):
    try:
        plus=int(plus)
    except:
        raise Http404()
    now=datetime.datetime.now()
    html="<html><body>%s houers from now will be %s</body></html>" % (plus ,now)
    return HttpResponse(html)
