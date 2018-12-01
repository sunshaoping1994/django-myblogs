from django.db import models

class Author(models.Model):
    """
    博客用户作者数据模型
    """
    id = models.AutoField(primary_key=True, verbose_name='作者编号')
    username = models.CharField(max_length=50, verbose_name='登录账户')
    userpass = models.CharField(max_length=50, verbose_name='登录密码')
    realname = models.CharField(max_length=20, verbose_name='作者姓名')
    header_img = models.ImageField(upload_to='static/images/headers/', default='static/images/headers/default.jpg')
    age = models.IntegerField(default=0, verbose_name='作者年龄')
    gender = models.CharField(max_length=5, verbose_name='作者性别', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='联系方式', null=True, blank=True)
    email = models.CharField(max_length=20, verbose_name='电子邮箱', null=True, blank=True)
    create_time = models.DateField(auto_now_add=True, verbose_name='注册时间')
    update_time = models.DateField(auto_now=True, verbose_name='最后修改时间')
    intro = models.TextField(verbose_name='个人介绍', null=True, blank=True)