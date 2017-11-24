# -*- coding: utf-8 -*-
from django.conf.urls import url

from api.views import *

urlpatterns = [
    url(r'^S', home_view),
]
