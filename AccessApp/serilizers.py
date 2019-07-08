from rest_framework import serializers
from .models import Access


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__' #全部序列
        #fields = ('username','passwd','gender','phone','address','user_img','user_status')
        #exclude = ('user_img',)#不包括头像
