from django.conf.urls import url
from DemoApp import views

urlpatterns = [
    #url(r'^index/',views.index,name='index'),
    url(r'^index_class/', views.IndexClass.as_view(), name='index_class'),
    #新增用户
    url(r'^user_create/',views.UserCreateView.as_view(),name='user_create'),
    #用户列表
    url(r'^user_list/',views.UserListView.as_view(),name='user_list'),
    #用户删除
    url(r'^user_delete/',views.UserDeleteView.as_view(),name='user_delete'),
    #用户编辑
    url(r'^user_update/',views.UserUpdateView.as_view(),name='user_update'),
]
