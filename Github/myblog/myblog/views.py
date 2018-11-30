# 首页视图处理模块
from django.shortcuts import render


# 首页视图处理函数
def index(request):
    return render(request, 'index.html')

