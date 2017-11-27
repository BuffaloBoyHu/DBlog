# -*- coding: utf-8 -*-
from django.conf.urls import url

from api.views import *

urlpatterns = [
    url(r'^$', home_view),
    url(r'^tag/(?P<id>\d+)/$', blog_filer_view, name='filterblog'),
    # 博客 添加，删除，修改，显示
    url(r'^add/$', blog_add_view, 'addblog'),
    url(r'^show/(?P<id>\d+)/$', blog_show_view, 'detailblog'),
    url(r'^update/(?P<id>\d+)/$', blog_update_view, 'updateblog'),
    url(r'^bloglist/$', blog_list_view, name='bloglist'),
]
