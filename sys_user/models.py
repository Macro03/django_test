from django.db import models
import datetime
# Create your models here.
class Department(models.Model):#对应一张表
    STATUS = [
        (1,'解冻状态'),
        (2,'冻结状态')
    ]
    depname = models.CharField(max_length=60,default='',verbose_name='部门名称')
    #create_time =models.DateTimeField(auto_created=True,)
    create_time = models.DateTimeField(default=datetime.datetime.now(),null=True)
    person_num = models.IntegerField(default=0)
    depstatus = models.IntegerField(choices=STATUS,default=1)
    detail = models.TextField(default='',verbose_name='描述')


class Stu(models.Model):
    name = models.CharField(max_length=30,default='',verbose_name='学生姓名')
    age = models.IntegerField(default=0,verbose_name='学生年龄')