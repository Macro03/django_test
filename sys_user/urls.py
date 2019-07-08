from django.conf.urls import url
from sys_user import views

urlpatterns = [
    url(r'^index_class/', views.IndexClass.as_view(), name='index_class'),
    url(r'^user_list/', views.UserList,name='user_list'),
]