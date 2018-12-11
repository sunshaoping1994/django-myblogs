# 作者路由模块
from django.conf.urls import url
from . import views


urlpatterns = [
    # 用户注册
    url(r'^register/$', views.author_register, name='author_register'),
    # 用户登录
    url(r'^login/$', views.author_login, name='author_login'),
    # 个人首页
    url(r'^(?P<author_id>\d+)/$', views.author_index, name='author_index'),
    # 用户退出
    url(r'^logout/$', views.author_logout, name='author_logout'),
    # 查看个人资料
    url(r'^(?P<author_id>\d+)/info/$', views.author_info, name='author_info'),
]
