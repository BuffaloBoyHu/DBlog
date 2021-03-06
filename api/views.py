# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __builtin__ import unicode
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import HttpResponse, render_to_response, render

# Create your views here.
from django.template import RequestContext

from api.blog_forms import BlogForm, TagForm
from api.models import Author, Blog, Tag


def home_view(request):
    return render_to_response('blog_list.html')


def blog_filer_view(request, id=None):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=id)
    blogs = tag.blog_set.all()
    return render_to_response("blog_filter.html",
                              {"blogs": blogs, "tag": tag, "tags": tags})


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
            return HttpResponseRedirect('/blog/show/%s' % id)
    else:
        form = BlogForm()
        tag = TagForm(initial={'tag_name': 'notags'})
    return render_to_response('blog_add.html',
                              {'form': form, 'tag': tag}, context_instance=RequestContext(request))


def blog_show_view(request, id):
    try:
        blog = Blog.objects.get(id=id)
        tags = Tag.objects.all()
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html",
                              {"blog": blog, "tags": tags},
                              context_instance=RequestContext(request))


def blog_update_view(request, id):
    id = id
    if request.method == 'POST':
        form = BlogForm(request.POST)
        tag = TagForm(request.POST)
        if form.is_valid() and tag.is_valid():
            cd = form.cleaned_data
            cdtag = tag.cleaned_data
            tagname = cdtag['tag_name']
            tagnamelist = tagname.split()
            for taglist in tagnamelist:
                Tag.objects.get_or_create(tag_name=taglist.strip())
            title = cd['caption']
            content = cd['content']
            blog = Blog.objects.get(id=id)
            if blog:
                blog.caption = title
                blog.content = content
                blog.save()
                for taglist in tagnamelist:
                    blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
                    blog.save()
                tags = blog.tags.all()
                for tagname in tags:
                    tagname = unicode(str(tagname), "utf-8")
                    if tagname not in tagnamelist:
                        notag = blog.tags.get(tag_name=tagname)
                        blog.tags.remove(notag)
            else:
                blog = Blog(caption=blog.caption, content=blog.content)
                blog.save()
            return HttpResponseRedirect('/blog/show/%s' % id)
    else:
        try:
            blog = Blog.objects.get(id=id)
        except Exception:
            raise Http404
        form = BlogForm(initial={'caption': blog.caption, 'content': blog.content}, auto_id=False)
        tags = blog.tags.all()
        if tags:
            taginit = ''
            for x in tags:
                taginit += str(x) + ' '
            tag = TagForm(initial={'tag_name': taginit})
        else:
            tag = TagForm()
    return render_to_response('blog_add.html',
                              {'blog': blog, 'form': form, 'id': id, 'tag': tag},
                              context_instance=RequestContext(request))


def blog_list_view(request):
    blogs = Blog.objects.order_by('-id')
    tags = Tag.objects.all()
    return render_to_response("blog_list.html",
                              {"blogs": blogs, "tags": tags, },
                              context_instance=RequestContext(request))
