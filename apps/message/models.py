from django.db import models

# Create your models here.

class UserMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name="用户名")
    email = models.EmailField(verbose_name="邮箱")
    address = models.CharField(max_length=200, verbose_name="地址")
    message = models.CharField(max_length=1000, verbose_name="留言信息")

    class Meta:
        verbose_name = "用户留言信息"
        verbose_name_plural = verbose_name