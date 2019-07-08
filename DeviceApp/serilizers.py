from .models import Temperature,Humidity,Carbondio,Pm25,Illumination
from rest_framework import serializers


class TemperSerializer(serializers.ModelSerializer):
    class Meta:

        model = Temperature

        fields = '__all__'#筛选全部列


class HumidSerializer(serializers.ModelSerializer):
    class Meta:

        model = Humidity

        fields = '__all__'#筛选全部列


class CarbonSerializer(serializers.ModelSerializer):
    class Meta:

        model = Carbondio

        fields = '__all__'#筛选全部列


class PmSerializer(serializers.ModelSerializer):
    class Meta:

        model = Pm25

        fields = '__all__'#筛选全部列


class IllumSerializer(serializers.ModelSerializer):
    class Meta:

        model = Illumination

        fields = '__all__'#筛选全部列