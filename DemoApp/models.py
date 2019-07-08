from django.db import models

# Create your models here.
class User(models.Model):
    username =  models.CharField(max_length=30,default='',verbose_name='用户名')
    passwd = models.CharField(max_length=255,default='',verbose_name='用户密码')
    gender = models.CharField(max_length=20,choices=(('male','男'),('female','女')),default='male',verbose_name='用户性别')
    phone = models.CharField(max_length=20,default='',verbose_name='联系方式')
    address = models.CharField(max_length=255,default='',verbose_name='地址')
    user_img = models.ImageField(upload_to='user/%Y',verbose_name='头像')
    user_status = models.IntegerField(choices=((1,'活跃'),(2,'禁用')),default=1,verbose_name='用户状态')

    def __str__(self):
        return self.username
