from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend, filters

from rest_framework import status,generics,filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .serilizers import AccessSerializer
from .models import Access

# Create your views here.
class IndexClass(APIView):
    def post(self, *args, **kwargs):
        return Response(data={'code':'200'},status=status.HTTP_200_OK)

#门禁管理：新增门禁记录
class AccessCreateView(generics.CreateAPIView):
    serializer_class = AccessSerializer
    queryset = Access.objects.all()
    def post(self, request, *args, **kwargs):
        accessserilizer = AccessSerializer(data = request.data)
        if accessserilizer.is_valid():
            #数据合法
            accessserilizer.save()#保存数据
            return Response(data={'code':200,'detail':'新增门禁成功'},status=status.HTTP_200_OK)
        else:#s数据不合法
            return Response(data={'code':400,'detail':'数据不合法'},status=status.HTTP_400_BAD_REQUEST)
