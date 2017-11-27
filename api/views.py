# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render_to_response

# Create your views here.
from django.template import RequestContext

from api.blog_forms import BlogForm, TagForm
from api.models import Author, Blog, Tag


def home_view(request):
    return HttpResponse('hellow this is blog')


def blog_filer_view(request, id):
    pass


def blog_add_view(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        tag = TagForm(request.POST)
        if form.is_valid() and tag.is_valid():
            cd = form.cleaned_data
            cdtag = tag.cleaned_data
            tagname = cdtag['tag_name']
            for taglist in tagname.split():
                Tag.objects.get_or_create(tag_name=taglist.strip())
            title = cd['caption']
            author = Author.objects.get(id=1)
            content = cd['content']
            blog = Blog(caption=title, author=author, content=content)
            blog.save()
            for taglist in tagname.split():
                blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
                blog.save()
            id = Blog.objects.order_by('-publish_time')[0].id
            return HttpResponseRedirect('/sblog/blog/%s' % id)
    else:
        form = BlogForm()


def