from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#温度列表
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics,filters
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Temperature,Humidity,Carbondio,Pm25,Illumination
from .serilizers import TemperSerializer,HumidSerializer,CarbonSerializer,PmSerializer,IllumSerializer

class IndexClass(APIView):
    def post(self, *args, **kwargs):
        return Response(data={'code':'200'},status=status.HTTP_200_OK)

class TemperCreateView(generics.CreateAPIView):
    """
    温度设备数据管理：新增温度数据

            温度数据管理:新增
            ---
            #### 字段说明 ：'*'表示接口调用必须
            |字段名称|描述|必须|类型|
            |--|--|--|--|
            |temper|温度值|*||
            |tem_time|温度记录时间|*|字符串|
            |tem_scene_id|温度场景识别码||字符串|
            |tem_status|温度设备状态||布尔类型：1为开启，2为关闭|

            #### 响应消息：
            |Http状态码|原因|响应模型|
            |--|--|--|
            |201|新增数据成功|信息描述|
            |400|请求参数有误|错误描述|
            |401|验证失败|信息描述|
            |403|权限错误|信息描述|
             """
    serializer_class = TemperSerializer
    queryset = Temperature.objects.all()
    def post(self, request, *args, **kwargs):
        temserilizer = TemperSerializer(data = request.data)
        if temserilizer.is_valid():#数据合法性验证
            # 数据合法
            temserilizer.save()#保存数据
            return Response(data={'code':200,'detail':'新增数据成功'},
                            status=status.HTTP_200_OK)

        else:#数据不合法
            return Response(data={'code':400,'detail':'数据不合法'},
                            status = status.HTTP_400_BAD_REQUEST)


#温度数据管理；列表展示（views/generics/mixin）
class TemperListView (generics.ListAPIView):
    """温度设备管理，列表展示"""
    queryset = Temperature.objects.all()
    serializer_class = TemperSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    search_fields = ('tem_scene_id','tem_time')#搜索


class HumidCreateView(generics.CreateAPIView):
    """
    湿度设备数据管理：新增湿度数据

            湿度数据管理:新增
            ---
            #### 字段说明 ：'*'表示接口调用必须
            |字段名称|描述|必须|类型|
            |--|--|--|--|
            |humid|湿度值|*||
            |hum_time|湿度记录时间|*|字符串|
            |hum_scene_id|湿度场景识别码||字符串|
            |hum_status|湿度设备状态||布尔类型：1为开启，2为关闭|

            #### 响应消息：
            |Http状态码|原因|响应模型|
            |--|--|--|
            |201|新增数据成功|信息描述|
            |400|请求参数有误|错误描述|
            |401|验证失败|信息描述|
            |403|权限错误|信息描述|
             """
    serializer_class = HumidSerializer
    queryset = Temperature.objects.all()
    def post(self, request, *args, **kwargs):
        humserilizer = HumidSerializer(data = request.data)
        if humserilizer.is_valid():#数据合法性验证
            # 数据合法
            humserilizer.save()#保存数据
            return Response(data={'code':200,'detail':'新增数据成功'},
                            status=status.HTTP_200_OK)

        else:#数据不合法
            return Response(data={'code':400,'detail':'数据不合法'},
                            status = status.HTTP_400_BAD_REQUEST)

#温度数据管理；列表展示（views/generics/mixin）
class TemperListView (generics.ListAPIView):
    """温度设备管理，列表展示"""
    queryset = Temperature.objects.all()
    serializer_class = TemperSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    search_fields = ('tem_scene_id','tem_time')#搜索
