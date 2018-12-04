from django.shortcuts import render, redirect
from django.http import HttpResponsePermanentRedirect
from . import models


def author_index(request, author_id):
    """
    个人首页
    :param request:
    :param author_id:
    :return:
    """
    author = models.Author.objects.get(pk=author_id)
    return render(request, 'author/index.html', {'author': author})


def author_register(request):
    """
    用户注册
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'author/register.html', {})
    elif request.method == "POST":
        # 获取用户数据
        username = request.POST.get('username')
        userpass = request.POST.get('userpass')
        re_userpass = request.POST.get('re_userpass')
        realname = request.POST.get('realname')
        # 判断用户信息
        try:
            # 判断用户名是否已经存在
            author = models.Author.objects.get(username=username)
            return render(request, 'author/register.html', {'error_msg': '账号已存在，请重新输入'})
        except:
            # 判断用户两次输入密码是否一致
            if userpass != re_userpass:
                return render(request, 'author/register.html', {'error_msg': '两次输入密码不一致，请重新输入'})
            # 保存用户信息
            author = models.Author(username=username, userpass=userpass, realname=realname)
            author.save()
            # 注册成功，跳转到登录页面
            return render(request, 'author/login.html', {'error_msg': '账号注册成功，请登录'})


def author_login(request):
    """
    用户登录
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'author/login.html', {})
    elif request.method == "POST":
        # 获取数据
        username = request.POST.get('username')
        userpass = request.POST.get('userpass')
        # 验证用户名和密码
        try:
            author = models.Author.objects.get(username=username, userpass=userpass)
            # 浏览器中记录用户session
            request.session['login_user'] = author
            # 浏览器关闭自动清除session
            request.session.set_expiry(0)
            print(author, type(author))
            return redirect('/')
        except:
            return render(request, 'author/login.html', {'error_msg': '用户账户或密码不正确，请重新输入'})


def author_logout(request):
    """
    用户退出
    :param request:
    :return:
    """
    request.session.clear()
    return redirect('/')






