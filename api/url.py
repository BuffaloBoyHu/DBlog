# -*- coding: utf-8 -*-
from django.conf.urls import url

from api.views import *

urlpatterns = [
    url(r'^$', home_view),
    url(r'^tag/(?P<id>\d+)/$', blog_filer_view, name='filterblog'),
    # 博客 添加，删除，修改
    url(r'^add/$', blog_add_view, 'addblog'),
]
