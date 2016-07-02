from django.shortcuts import render
from django.template import RequestContext, loader
import json

from grillmoncontroller import Thermocouple

# Create your views here.

from django.http import HttpResponse

def format_decimal(x):
    try:
        return "%0.1f" % x
    except:
        return ""

def index(request):
    template = loader.get_template('grillmonui/index.html')
    context = RequestContext(request, {});
    return HttpResponse(template.render(context))

def getTemp(request):
    (fault, internalC, externalC) = Thermocouple.readThermo()
    result = {"externalF": format_decimal(Thermocouple.to_f(externalC)),
              "fault": Thermocouple.fault,
              "internalF": format_decimal(Thermocouple.to_f(internalC))}

    return HttpResponse(json.dumps(result), content_type='application/javascript')


