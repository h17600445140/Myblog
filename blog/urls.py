#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.urls import path,re_path
from blog import views
# app_name='blog'
app_name = '[blog]'
urlpatterns=[
    path('index/',views.view_index),
    re_path(r'page/(\d+)',views.view_index,name='page'),
    re_path(r'page/content/(\d+)',views.post_content,name='content'),
    re_path(r'category/(\d+)',views.category_view),
    re_path(r'archive/(\d+)/(\d+)',views.date_view),
    path('search/',views.search_view),

]