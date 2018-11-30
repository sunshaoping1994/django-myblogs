"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 注册子路由
    url(r'^album/', include('album.urls')),
    url(r'^article/', include('article.urls')),
    url(r'^author/', include('author.urls')),
    url(r'^authorsay/', include('authorsay.urls')),
    url(r'^comment/', include('comment.urls')),
    url(r'^message/', include('message.urls')),
    url(r'^photo/', include('photo.urls')),
]
