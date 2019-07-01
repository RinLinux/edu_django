from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UsersProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称",default='')
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(choices=(('male','男'),('female','女')),default='female')
    address = models.CharField(max_length=10,default='',verbose_name='地址')
    mobile = models.CharField(max_length=11,verbose_name='手机号码')