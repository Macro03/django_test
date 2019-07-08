from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class IndexClass(APIView):
    def post(self, *args, **kwargs):
        return Response(data={'code':'200'},status=status.HTTP_200_OK)



#用户列表
def UserList(request):
    #return HttpResponse("hello word")
    stus = ['aa','bb','cc','dd']
    return render(request,'userlist.html',context={
        'name':'zhangsan',
        'age':18,
        'stus':stus
    })