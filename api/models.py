# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Author(models.Model):
    class Meta:
        verbose_name = '作者'

    name = models.CharField(max_length=20, verbose_name="称呼")
    email = models.EmailField(verbose_name='邮箱', default="wwww@zhizi.com")
    descript = models.TextField(verbose_name='个人描述')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", null=True)
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间', null=True)


class Tag(models.Model):
    class Meta:
        verbose_name = '标签'

    name = models.CharField(max_length=20, verbose_name='标签名')
    sub_name = models.CharField(max_length=30, verbose_name='子标签', default='kkkk', blank=True, null=True)
    level = models.IntegerField(verbose_name='等级', default=2, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", null=True)
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间', null=True)


class Blog(models.Model):
    class Meta:
        verbose_name = '博客'

    caption = models.CharField(max_length=50, verbose_name='标题')
    author = models.ForeignKey(Author, verbose_name='作者')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    content = models.TextField(verbose_name='内容')
    recommend = models.BooleanField(default=False, verbose_name='推荐')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", null=True)
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间', null=True)
