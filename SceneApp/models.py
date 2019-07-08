import datetime
from django.db import models

# Create your models here.
class Scene(models.Model):
    sce_name =  models.CharField(max_length=30,default='',verbose_name='场景名称')
    sce_id = models.AutoField(verbose_name='场景识别码',primary_key=True)
    sce_passwd = models.CharField(max_length=255, default='', verbose_name='场景密码')
    sce_status = models.IntegerField(choices=((1, '在线'), (2, '离线')), default=2, verbose_name='场景状态')
    sce_info = models.TextField(default='',verbose_name='场景描述')
    devnum = models.IntegerField(default=0,verbose_name='设备数量')
    create_time = models.DateTimeField(default=datetime.datetime.now(), null=True,verbose_name='接入时间')
    sce_pri = models.IntegerField(default=0,verbose_name='优先级')
    sce_area = models.FloatField(default=0.0,verbose_name='管理面积')

    def __str__(self):
        return self.sce_name

#场景环境状态
class SceneEnvir(models.Model):
    rec_time = models.DateTimeField(default=datetime.datetime.now(), null=True,verbose_name='记录时间')
    sce_temp = models.FloatField(default=0.0,verbose_name='温度')
    sce_humid = models.FloatField(default=0.0,verbose_name='湿度')
    sce_CO2 = models.IntegerField(default=0,verbose_name='CO2')
    sce_PM = models.FloatField(default=0.0,verbose_name='PM2.5')
    sce_light = models.FloatField(default=0.0,verbose_name='光照强度')
    #场景识别码
    sce_id = models.ForeignKey(Scene,verbose_name='场景识别码')
#场景安防状态
class SceneSave(models.Model):
    STATUS = [
        (1, '正常'),
        (2, '异常')
    ]
    rec_time = models.DateTimeField(default=datetime.datetime.now(), null=True, verbose_name='记录时间')
    sce_smog = models.IntegerField(choices=STATUS,verbose_name='烟雾传感器')
    sce_methane = models.IntegerField(choices=STATUS,verbose_name='甲烷传感器')
    sce_fire = models.IntegerField(choices=STATUS,verbose_name='火光传感器')
    sce_IDS = models.IntegerField(choices=STATUS,verbose_name='入侵检测')
    #场景识别码
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')
