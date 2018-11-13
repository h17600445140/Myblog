#!/usr/bin/env python
# -*- coding:utf-8 -*-
from blog.models import *
from django.db.models import *
from datetime import *

def globla_context_process(request):
    content={}
    content['category'] = Post.objects.values('category','category__name').annotate(count = Count('*'))
    # print(content['category'])
    # [{'category': 1, 'category__name': 'Django', 'count': 1}, {'category': 2, 'category__name': 'Models', 'count': 1}

    archive = get_archive()
    # archive = Post.objects.values('created').order_by('-created')
    content['archive']=archive
    # print(content['archive'])
    # [{'created': datetime.date(2018, 11, 1), 'count': 4}]

    content['recent']=Post.objects.order_by('-created').all()[:2]
    # print(content['recent'])
    # [ < Post: 初始Django >, < Post: models详解 >]

    # 全局上下文返回必须是个类字典
    return content

def get_archive():
    s = set()
    for t in Post.objects.values('created'):
        s.add(str(t['created'].year) + "-" + str(t['created'].month))   #去重
    archive = []
    for time in s:
        year = time.split('-')[0]
        month = time.split('-')[1]
        item = {'created': date(year=int(year), month=int(month), day=1),
                'count': Post.objects.filter(created__year=year, created__month=month).count()}
        archive.append(item)
    return archive