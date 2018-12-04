# 首页视图处理模块
from django.shortcuts import render
from author.models import Author


# 首页视图处理函数
def index(request):
    author_list = Author.objects.all().order_by('-create_time')[:4]
    return render(request, 'index.html', {'author_list': author_list})

