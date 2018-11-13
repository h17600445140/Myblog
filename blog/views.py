from django.shortcuts import render

# Create your views here.
from blog.models import *
# 主界面函数
def view_index(request,num='1'):
    page,page_range = Post.get_posts_by_page(num)   #分页处理
    return render(request,'index.html',{'page':page,'page_range':page_range})

def post_content(request,id):
    try:
        post = Post.objects.get(id=id)
    except:
        pass
    return render(request,'content.html',{'post':post})

def category_view(request,category_id):
    posts = Post.objects.filter(category=category_id).order_by('-created')   #传过来的id不一样，代表不同类别的贴子
    return render(request,'archive.html',{'posts':posts})

def date_view(request,year,month):
    posts = Post.objects.filter(created__year=year,created__month=month).all()
    # print(111)
    # print(posts)
    # print(111)
    # < QuerySet[ < Post: models详解 >, < Post: Views详解 >, < Post: Templates详解 >, < Post: Django初识 >] >
    return render(request, 'archive.html', {'posts': posts})

from haystack.models import SearchResult
from haystack.query import SearchQuerySet
from haystack.query import SQ
from  django.core.paginator import  Paginator
def search_view(request):

    # ————————————————————————————————————
    # search_result = SearchQuerySet().filter(SQ(title = request.GET.get('q'))).all()
    # paginator = Paginator(search_result,10)

    # posts = paginator.page(1).object_list
    # print(222)
    # print(posts)
    # print(222)
    # [ < SearchResult: blog.post(pk='4') >]

    # page = paginator.page(1)
    # posts = []
    # for result in page.object_list:
    #     posts.append(result.object)
    # ————————————————————————————————————————————————————————
    # search_result = SearchQuerySet().filter(SQ(title=request.GET.get('q')) | SQ(content=request.GET.get('q'))).all()
    # print(111)
    # print(search_result)
    # print(111)
    # < SearchQuerySet: query = < haystack.backends.whoosh_backend.WhooshSearchQueryobjectat0x0000020DE155C2E8 >, using = None >
    # posts = []
    # for result in search_result:
    #     posts.append(result.object)
    # ————————————————————————————————————————

    keyword = request.GET.get('q')
    paginator = Paginator(SearchQuerySet().filter(SQ(title=keyword) | SQ(content=keyword)).all(), 10)
    page = paginator.page(1)
    posts = []

    for result in page.object_list:
        posts.append(result.object)
    return render(request,'archive.html',{'posts': posts})
