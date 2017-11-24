# -*- coding: utf-8 -*-
from django.conf.urls import url

from api.views import *

urlpatterns = [
    url(r'^$', home_view),
    url(r'^api/$', home_h_view),
]
