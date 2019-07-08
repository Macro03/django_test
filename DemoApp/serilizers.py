from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = '__all__' #全部序列
        #fields = ('username','passwd','gender','phone','address','user_img','user_status')
        exclude = ('user_img',)#不包括头像

class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)#添加字段
    class Meta:
        model = User
        #fields = '__all__' #全部序列
        fields = ('id','username','passwd','gender','phone','address','user_status')
        #exclude = ('user_img',)#不包括头像