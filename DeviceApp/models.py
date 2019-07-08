from django.db import models
from SceneApp.models import Scene
# Create your models here.
STATUS = [
    (1, '正常'),
    (2, '异常'),
]
#温度传感器
class Temperature(models.Model):
    temper = models.IntegerField(default=0,verbose_name='温度值(°C)')
    tem_time = models.DateTimeField(verbose_name='温度记录时间',auto_now_add=True)
    tem_status = models.IntegerField(choices=((1,'开启'),(2,'关闭')),default=1,verbose_name='温度设备状态')
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')

#湿度传感器
class Humidity(models.Model):
    humid = models.IntegerField(default=0,verbose_name='湿度值(%)')
    hum_time = models.DateTimeField(verbose_name='湿度记录时间',auto_now_add=True)
    hum_status = models.IntegerField(choices=((1,'开启'),(2,'关闭')),default=1,verbose_name='湿度设备状态')
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')

#CO2传感器
class Carbondio(models.Model):
    carbondio = models.IntegerField(default=0,verbose_name='二氧化碳含量(PPM)')
    carb_time = models.DateTimeField(verbose_name='二氧化碳记录时间',auto_now_add=True)
    car_status = models.IntegerField(choices=((1,'开启'),(2,'关闭')),default=1,verbose_name='CO₂设备状态')
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')

#PM2.5传感器
class Pm25(models.Model):
    pm25 = models.IntegerField(default=0,verbose_name='PM2.5(μg/m³)')
    pm_time = models.DateTimeField(verbose_name='PM2.5记录时间',auto_now_add=True)
    pm_status = models.IntegerField(choices=((1,'开启'),(2,'关闭')),default=1,verbose_name='PM2.5设备状态')
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')

#光强传感器
class Illumination(models.Model):
    illu = models.IntegerField(default=0,verbose_name='光照强度(lx)')
    ill_time = models.DateTimeField(verbose_name='光强记录时间',auto_now_add=True)
    ill_status = models.IntegerField(choices=((1,'开启'),(2,'关闭')),default=1,verbose_name='光强设备状态')
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')

#烟雾传感器
class Smog(models.Model):
    smog_time = models.DateTimeField(verbose_name='烟雾告警记录时间', auto_now_add=True)
    smog_status = models.IntegerField(choices=STATUS, default=1, verbose_name='烟雾状态')
    dev_status = models.IntegerField(choices=((1,'开启'),(2,'关闭')),default=1,verbose_name='设备状态')
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')

#甲烷传感器
class Methane(models.Model):
    meth_time = models.DateTimeField(verbose_name='甲烷告警记录时间', auto_now_add=True)
    meth_status = models.IntegerField(choices=STATUS, default=1, verbose_name='甲烷状态')
    dev_status = models.IntegerField(choices=((1,'开启'),(2,'关闭')),default=1,verbose_name='设备状态')
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')

#火光传感器
class Fire(models.Model):
    fire_time = models.DateTimeField(verbose_name='火光告警记录时间', auto_now_add=True)
    fire_status = models.IntegerField(choices=STATUS, default=1, verbose_name='火光状态')
    dev_status = models.IntegerField(choices=((1,'开启'),(2,'关闭')),default=1,verbose_name='设备状态')
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')

#报警灯
class WarnLight(models.Model):
    warn_time = models.DateTimeField(verbose_name='报警灯亮时间', auto_now_add=True)
    dev_status = models.IntegerField(choices=((1, '开启'), (2, '关闭')), default=1, verbose_name='设备状态')
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')

#报警器
class WarnBuzzer(models.Model):
    warn_time = models.DateTimeField(verbose_name='报警灯亮时间', auto_now_add=True)
    dev_status = models.IntegerField(choices=((1, '开启'), (2, '关闭')), default=1, verbose_name='设备状态')
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')

#水泵
class WaterPump(models.Model):
    dev_status = models.IntegerField(choices=((1, '开启'), (2, '关闭')), default=1, verbose_name='设备状态')
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')

#灯光
class Light(models.Model):
    dev_status = models.IntegerField(choices=((1, '开启'), (2, '关闭')), default=1, verbose_name='设备状态')
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')

#风机
class DraughtFan(models.Model):
    dev_status = models.IntegerField(choices=((1, '开启'), (2, '关闭')), default=1, verbose_name='设备状态')
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')

#LED显示器
class LED(models.Model):
    dev_status = models.IntegerField(choices=((1, '开启'), (2, '关闭')), default=1, verbose_name='设备状态')
    dev_context = models.TextField(default='',verbose_name='显示内容')
    sce_id = models.ForeignKey(Scene, verbose_name='场景识别码')