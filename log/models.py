from django.db import models
import  datetime
# Create your models here.
class Log(models.Model):
    log_module = models.CharField(max_length=60,default='',verbose_name='操作模块')
    log_addtime = models.DateTimeField(default=datetime.datetime.now(),verbose_name='创建时间')
    log_context = models.CharField(max_length=255,default='',verbose_name='操作内容')
    log_ip = models.CharField(max_length=20,default='',verbose_name='操作ip')
    log_user = models.CharField(max_length=255,default='',verbose_name='操作人员')