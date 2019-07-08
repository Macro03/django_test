from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend, filters
from .schemas import DeleteUserSchema
from rest_framework import status,generics,filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .serilizers import UserSerializer,UserUpdateSerializer
from .models import User
from log.views import addLog

class IndexClass(APIView):
    def post(self, *args, **kwargs):
        return Response(data={'code':'200'},status=status.HTTP_200_OK)


#用户管理：新增用户
class UserCreateView(generics.CreateAPIView):
    """
    #### 字段说明 ：'*'表示接口调用必须
    | 字段名称 | 描述 | 必须 | 类型 |
    | -- | -- | -- | -- |
    | username | 用户账号 | * | 字符串 |
    | password | 密码 | * | 字符串 |
    | last_name | 用户姓名 | * | 字符串 |
    | is_active | 账户是否可用 | | 布尔类型，默认为：1
    启用0禁用 |
    | user_tel | 用户电话 | | 字符串 |
    | user_address | 用户地址 | | 字符串 |
    | user_number | 用户工号 | | 字符串 |
    | user_gender | 用户性别: male / female | | 字符串 |
    | email | 用户邮箱 | | 字符串 |

    #### 响应消息：
    | Http状态码 | 原因 | 响应模型 |
    | -- | -- | -- |
    | 201 | 新增用户成功 | 信息描述 |
    | 400 | 请求的参数有误 | 错误描述 |
    | 401 | 用户验证失败 | 信息描述 |
    | 403 | 权限错误 | 信息描述 |
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        userserilizer = UserSerializer(data = request.data)
        if userserilizer.is_valid():
            #数据合法
            userserilizer.save()#保存数据
            return Response(data={'code':200,'detail':'新增用户成功'},status=status.HTTP_200_OK)
        else:#s数据不合法
            return Response(data={'code':400,'detail':'数据不合法'},status=status.HTTP_400_BAD_REQUEST)

#用户管理：列表展示
class UserListView(generics.ListAPIView):
    '''用户管理：列表展示'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    search_fields = ('username','address')

#用户管理：删除用户（不采用序列化，以及generics）
class UserDeleteView(APIView):
    """
    用户管理：删除用户
    """
    schema = DeleteUserSchema
    def post(self,request):#拿到的数据都在request.data
        user_id = request.data.get('user_id',None)
        if user_id is None:
            return Response(data={'code':400,'detail':'缺少参数'})
        #根据用户编号查找对应的用户
        try:
            user_result = User.objects.get(id=user_id)
            #删除操作
            result = user_result.delete()
            if result:
                return Response(data={'code': 200, 'detail': '删除成功'})
            else:
                return Response(data={'code': 400, 'detail': '删除失败'})
        except Exception as e:
            return Response(data={'code':400,'detail':'用户不存在'})
        #return Response(data={'code': 200, 'detail': '没什么用'})
        # 判断是否存在用户
        #if user_result:

#用户管理：编辑用户
class UserUpdateView(generics.GenericAPIView):
    '''
    用户管理:编辑用户
    '''
    serializer_class = UserUpdateSerializer
    def post(self,request):
        #接收数据
        user_id = request.data.get('id',None)
        if user_id is None:
            return  Response(data={'code':400,'detail':'缺少参数'})
        try:
            updateuser = User.objects.get(id=user_id)
            print(user_id)
            #把数据形成序列化
            userserialize = UserUpdateSerializer(data = request.data)
            if userserialize.is_valid():
                #修改数据，参数是否合法
                userserialize.update(instance=updateuser,validated_data=request.data)
                return Response(data={'code':200,'detail':'修改成功'})
            else:
                return Response(data={'code':400,'detail':'数据不合法'})
        except Exception as e:
            return Response(data={'code':400,'detail':'用户不存在'})

        #return Response(data={'code':200})