from django.conf.urls import url

from DeviceApp import views

urlpatterns = [

    url(r'^index_class/', views.IndexClass.as_view(), name='index_class'),

    #温度列表创建
    url(r'^temper_create/',views.TemperCreateView.as_view(),name='temper_create'),

    # 湿度列表创建
    url(r'^humid_create/', views.HumidCreateView.as_view(), name='humid_create'),

    # # CO2列表创建
    # url(r'^carbon_create/', views.CarbonCreateView.as_view(), name='carbon_create'),
    #
    # # PM2.5列表创建
    # url(r'^pm25_create/', views.PmCreateView.as_view(), name='pm25_create'),
    #
    # # 光强列表创建
    # url(r'^illum_create/', views.IllumCreateView.as_view(), name='illum_create'),
    #
    #
    # #温度列表展示--------------------------------------------------------------------------
    # url(r'^temper_list/',views.TemperListView.as_view(),name='temper_list'),
    #
    # # 湿度列表展示
    # url(r'^temper_list/', views.HumidListView.as_view(), name='temper_list'),
    #
    # # CO2列表展示
    # url(r'^temper_list/', views.TemperListView.as_view(), name='temper_list'),
    #
    # # PM2.5列表展示
    # url(r'^temper_list/', views.TemperListView.as_view(), name='temper_list'),
    #
    # # 光强列表展示
    # url(r'^temper_list/', views.TemperListView.as_view(), name='temper_list')
]