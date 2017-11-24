# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse


# Create your views here.

def home_view(request):
    return HttpResponse('hellow this is blog')


def home_h_view(request):
    return HttpResponse('hellow this isasdasdsdasdasd blog')