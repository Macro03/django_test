from rest_framework import serializers
from .models import Scene,SceneEnvir,SceneSave


class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        #fields = '__all__' #全部序列
        #fields = ('username','passwd','gender','phone','address','user_img','user_status')
        exclude = ('create_time',)#不包括头像

class SceneUpdateSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(required=True)#添加字段
    class Meta:
        model = Scene
        #fields = '__all__' #全部序列
        fields = ('sce_name','sce_id','sce_passwd','sce_status','sce_info','devnum','create_time','sce_pri','sce_area')
        #exclude = ('user_img',)#不包括头像

class SceneEnvirSerializer(serializers.ModelSerializer):
    class Meta:
        model = SceneEnvir
        fields = '__all__' #全部序列
        #fields = ('username','passwd','gender','phone','address','user_img','user_status')
        #exclude = ('create_time',)#不包括头像

class SceneSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SceneSave
        fields = '__all__' #全部序列
        #fields = ('username','passwd','gender','phone','address','user_img','user_status')
        #exclude = ('create_time',)#不包括头像
