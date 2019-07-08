from django.db import models
import datetime
from django.db import models

# Create your models here.

class Access(models.Model):
    apply_name =  models.CharField(max_length=30,default='',verbose_name='申请人名称')
    #verify_name = models.CharField(max_length=30, default='', verbose_name='审核人名称')
    apply_phone = models.CharField(max_length=20, default='', verbose_name='联系方式')
    apply_status = models.IntegerField(choices=((1, '未审核'), (2, '已审核')), default=1, verbose_name='用户状态')
    sce_id = models.CharField(max_length=255,default='',verbose_name='场景识别码')
    apply_detail = models.TextField(default='',verbose_name='来访原由')
    visit_peo = models.TextField(default='', verbose_name='随行人员')
    #apply_Inc = models.CharField(max_length=255, default='', verbose_name='所属公司')
    start_time = models.DateTimeField(default=datetime.datetime.now(),null=True,verbose_name='来访时间')
    end_time = models.DateTimeField(default=datetime.datetime.now(),null=True, verbose_name='离开时间')

    def __str__(self):
        return self.apply_name


'''
class Verify(models.Model):
    verify_name = models.CharField(max_length=30, default='', verbose_name='审核人名称')
'''