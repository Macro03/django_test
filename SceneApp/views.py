from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend, filters
from .schemas import DeleteSceneSchema
from rest_framework import status,generics,filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .serilizers import SceneSerializer,SceneUpdateSerializer,SceneEnvirSerializer,SceneSaveSerializer
from .models import Scene,SceneSave,SceneEnvir
# Create your views here.

class IndexClass(APIView):
    def post(self, *args, **kwargs):
        return Response(data={'code':'200'},status=status.HTTP_200_OK)

#场景管理：新增场景
class SceneCreateView(generics.CreateAPIView):
    serializer_class = SceneSerializer
    queryset = Scene.objects.all()
    def post(self, request, *args, **kwargs):
        sceneserilizer = SceneSerializer(data = request.data)
        if sceneserilizer.is_valid():
            #数据合法
            sceneserilizer.save()#保存数据
            return Response(data={'code':200,'detail':'新增场景成功'},status=status.HTTP_200_OK)
        else:#s数据不合法
            return Response(data={'code':400,'detail':'数据不合法'},status=status.HTTP_400_BAD_REQUEST)

#场景管理：列表展示
class SceneListView(generics.ListAPIView):
    queryset = Scene.objects.all()
    serializer_class = SceneSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    search_fields = ('sce_name','sce_id')

#场景管理：删除场景（不采用序列化，以及generics）
class SceneDeleteView(APIView):
    """
    用户管理：删除用户
    """
    schema = DeleteSceneSchema
    def post(self,request):#拿到的数据都在request.data
        sce_id = request.data.get('scene_id',None)
        if sce_id is None:
            return Response(data={'code':400,'detail':'缺少参数'})
        #根据场景编号查找对应的场景
        try:
            sce_result = Scene.objects.get(id=sce_id)
            #删除操作
            result = sce_result.delete()
            if result:
                return Response(data={'code': 200, 'detail': '删除成功'})
            else:
                return Response(data={'code': 400, 'detail': '删除失败'})
        except Exception as e:
            return Response(data={'code':400,'detail':'场景不存在'})
        #return Response(data={'code': 200, 'detail': '没什么用'})
        # 判断是否存在用户
        #if user_result:

#用户管理：编辑用户
class SceneUpdateView(generics.GenericAPIView):
    '''
    用户管理:编辑用户
    '''
    serializer_class = SceneUpdateSerializer
    def post(self,request):
        #接收数据
        qsce_id = request.data.get('sce_id',None)
        if qsce_id is None:
            return  Response(data={'code':400,'detail':'缺少参数'})
        try:
            updatesce = Scene.objects.get(sce_id=qsce_id)
            print(qsce_id)
            #把数据形成序列化
            sceserialize = SceneUpdateSerializer(data = request.data)
            if sceserialize.is_valid():
                #修改数据，参数是否合法
                sceserialize.update(instance=updatesce,validated_data=request.data)
                return Response(data={'code':200,'detail':'修改成功'})
            else:
                return Response(data={'code':400,'detail':'数据不合法','error':sceserialize.errors[list(sceserialize.errors.keys())[0]][0]})

        except Exception as e:
            return Response(data={'code':400,'detail':'场景不存在'})

        #return Response(data={'code':200})

#场景环境：新增


#场景环境：列表展示 直接展示不需要查询？
class SceneEnvirListViwe(generics.ListAPIView):
    queryset = SceneEnvir.objects.all()
    serializer_class = SceneEnvirSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('sce_id')

#场景安防：新增

#场景安防：列表展示