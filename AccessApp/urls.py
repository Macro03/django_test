from django.conf.urls import url
from AccessApp import views

urlpatterns = [
    #url(r'^index/',views.index,name='index'),
    url(r'^index_class/', views.IndexClass.as_view(), name='index_class'),
    #新增门禁记录
    url(r'^access_create/',views.AccessCreateView.as_view(),name='access_create'),

]
